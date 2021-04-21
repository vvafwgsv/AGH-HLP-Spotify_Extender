import sys, os, spotipy
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath, QColor
from PyQt5.QtWidgets import QGraphicsEffect, QGraphicsOpacityEffect, QGraphicsDropShadowEffect, QPushButton

from bck.Album import Album
from bck.SpotifyClient import SpotifyClient
from py_source.main_window import Ui_entryWindow
from py_source.final_window import Ui_mainWindow
from py_source.custom_dialog import Ui_Dialog
from subclasses.album_button import album_button
from support.Oauth2Manager import Oauth2Manager
from support.VerifyToken import VerifyToken
from support.acquireImage import AcquireImage, is_saved, get_path


# prior to the following token was cached at venv dir
caches_folder = '../../.spotify_caches/'


if not os.path.exists(caches_folder):
    os.makedirs(caches_folder)


def session_cache_path():
    return caches_folder + "cache"



class entWin(QtWidgets.QMainWindow):
    counter = 0
    successful_auth = False

    def __init__(self):
        self.spotify = None
        self._old_pos = None

        QtWidgets.QMainWindow.__init__(self)

        self.ui = Ui_entryWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.show()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.load)

        # hide progbar
        self.ui.pb1.setVisible(False)

        # connect event listeners:
        self.ui.exitButton.clicked.connect(self.quit_window)
        self.ui.triggerButton.clicked.connect(self.initiate_OAuth2)

    def load(self):
        self.ui.pb1.setValue(self.counter)

        # close window on fin
        if self.counter > 100:
            self.timer.stop()
            # if the bar is loaded, close this window and load main app window supplied with spotify data
            if self.successful_auth:
                self.main = mainWin(self.spotify, self.spotify_client)
                self.main.show()
                # close splash
                self.close()
            else:
                self.reset_trig()
                self.reset_progbar()

        self.counter += 1

    def quit_window(self):
        self.close()

    def initiate_OAuth2(self):

        self.ui.triggerButton.setVisible(False)
        self.ui.triggerButton.setDisabled(True)
        self.ui.pb1.setVisible(True)
        self.timer.start(15)

        cache_handler = spotipy.cache_handler.CacheFileHandler(cache_path=session_cache_path())
        sp_oauth = Oauth2Manager().create_spotify_oauth(cache_handler)
        self.spotify = spotipy.Spotify(auth_manager=sp_oauth)
        print(self.spotify.me())

        try:
            verify_token = VerifyToken(session_cache_path())
            if not verify_token.get_status():
                verify_token.refresh_token()

            else:
                print(verify_token.auth_manager.get_cached_token())
                self.successful_auth = True
                self.spotify_client = SpotifyClient(
                    verify_token.auth_manager.get_cached_token()['access_token'],
                    self.spotify.me()['id']
                )
        except TypeError as e:
            print(e)

    def reset_progbar(self):
        self.ui.pb1.setValue(0)
        self.ui.pb1.setVisible(True)
        self.ui.pb1.setDisabled(False)

    def reset_trig(self):
        self.ui.triggerButton.setValue(0)
        self.ui.triggerButton.setVisible(True)
        self.ui.triggerButton.setDisabled(False)

    # introduce window dragging mechanism; overriding Qt methods
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = event.pos() - self._old_pos
        self.move(self.pos() + delta)


class mainWin(QtWidgets.QMainWindow):
    def __init__(self, spotify, handle_spotify):
        self._old_pos = None
        self.spotify = spotify
        self.handle_spotify = handle_spotify
        # self.counter = 0

        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.music_stacked.setCurrentWidget(self.ui.init_search_page)
        self.ui.rmv_stacked.setCurrentWidget(self.ui.rmv_choose_playlist)

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.widget.setGraphicsEffect(QGraphicsOpacityEffect().setOpacity(0.1))

        ####### SET SPOTIFY ACCOUNT PARAMS
        self.ui.thefuck.setText(
            f"public playlists: "
            + str(len(self.spotify.current_user_playlists(limit=50)['items']))
            + ". Followers " + str(self.spotify.me()['followers']['total'])
        )

        ####### SET AVATAR
        if not is_saved(self.spotify.me()["display_name"]):
            AcquireImage(self.spotify.me()["images"][0]["url"], self.spotify.me()["display_name"])

        _pixmap = QPixmap(get_path(self.spotify.me()["display_name"]))

        self.ui.avatar.setScaledContents(True)

        ####### IF FETCHED AVA IS SMALLER THAN 200X200
        if _pixmap.width() < self.ui.avatar.width() or _pixmap.height() < self.ui.avatar.height():
            _pixmap.scaled(
                self.ui.avatar.width(),
                self.ui.avatar.height(),
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation
            )
        else:
            _pixmap.scaled(
                self.ui.avatar.width(),
                self.ui.avatar.height(),
                Qt.AspectRatioMode.KeepAspectRatio
            )
        ###### ROUND THIS FUCKER; STYLESHEETS WONT WORK;
        ###### STYLESHEETS APPLIED TO LABEL WONT COVER ITS CONTENT
        ###### https://stackoverflow.com/questions/61147963/pyqt5-keeping-image-from-overflowing-qlabel
        _target = QPixmap(200, 200)
        _target.fill(Qt.transparent)

        _painter = QPainter(_target)
        _painter.setRenderHint(QPainter.Antialiasing, True)
        _painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
        _painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        _path = QPainterPath()
        _path.addRoundedRect(
            0, 0, self.ui.avatar.width(), self.ui.avatar.height(), 100, 100
        )
        _painter.setClipPath(_path)
        _painter.drawPixmap(-20,-20, _pixmap)  # by trial and error
        _painter.end()
        self.ui.avatar.setPixmap(_target)

        ####### SET ICONS - DESIGNER DOES NOT COOPERATE
        _pixmap = QPixmap("./ui_source/ref1.png")
        _pixmap.scaled(
            self.ui.rmv_icon.width(),
            self.ui.rmv_icon.height(),
            Qt.AspectRatioMode.KeepAspectRatio
        )
        self.ui.rmv_icon.setPixmap(_pixmap)
        self.ui.rmv_icon.setScaledContents(True)

        _pixmap = QPixmap("./ui_source/ref2.png")
        _pixmap.scaled(
            self.ui.music_icon.width(),
            self.ui.music_icon.height(),
            Qt.AspectRatioMode.KeepAspectRatio
        )
        self.ui.music_icon.setPixmap(_pixmap)
        self.ui.music_icon.setScaledContents(True)

        # disable mac focus on qline
        self.ui.init_line_edit.setAttribute(Qt.WA_MacShowFocusRect,0)
        self.ui.rmv_line_edit.setAttribute(Qt.WA_MacShowFocusRect,0)

        ###### SET ACTIONS

        ###### MAIN WINDOW
        self.ui.exitButton.clicked.connect(self.quit_window)

        ###### STACKED-MAIN: FOCUSED ON BY DEFAULT
        self.ui.welcomeLabel.setText(self.spotify.me()["display_name"])
        # self.ui.thefuck.setText() <- set num of pub playlists, following, followers

        ###### CHANGE STACKED -> MUSIC_PAGE ON  CLICK
        self.ui.music_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.music_page))

        ###### CHANGE STACKED -> RMV_PAGE ON  CLICK
        self.ui.rmv_btn.clicked.connect(self.populate_rmv_scroll_panel)

        ###### STACKED-MUSIC:
        self.ui.exit_music.clicked.connect(lambda: self.reset_music_stacked(self.ui.init_search_page, self.ui.main_page))
        self.ui.init_error_label.setVisible(False)  # hide error label

        ###### MUSIC-STACKED:
        self.ui.init_search.clicked.connect(self.init_search)

        ###### SEARCH-STACKED:
        self.ui.reload_result.clicked.connect(lambda: self.ui.music_stacked.setCurrentWidget(self.ui.init_search_page))

        ###### STACKED-RM
        self.ui.exit_rmv.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.main_page))

        ###### SEARCH-STACKED:
        self.ui.exit_choose.clicked.connect(lambda: self.ui.music_stacked.setCurrentWidget(self.ui.init_search_page))

        ###### SET PLAYLIST BUTTONS WITH HANDLES

        self.show()

    def reset_music_stacked(self, substack_to_set, stack_to_set):
        if self.ui.init_error_label.isVisible():
            self.ui.init_error_label.setVisible(False)
        self.ui.init_line_edit.clear()
        self.ui.stackedWidget.setCurrentWidget(stack_to_set)
        self.ui.music_stacked.setCurrentWidget(substack_to_set)

    def music_stacked_to_init(self):
        if self.ui.init_error_label.isVisible():
            self.ui.init_error_label.setVisible(False)
        self.ui.init_line_edit.clear()
        self.ui.music_stacked.setCurrentWidget(self.ui.init_search_page)

    def init_search(self):
        _successful = False
        _albums = None
        if self.ui.init_line_edit.text() != "":
            _albums = self.handle_spotify.search_for_album(self.ui.init_line_edit.text(), "")
        if not _albums:
            self.ui.init_line_edit.clear()
            self.ui.init_error_label.setVisible(True)
        else:
            self.ui.music_stacked.setCurrentWidget(self.ui.choose_search)
            self.ui.init_line_edit.clear()
            self.populate_choose_search(_albums)

    # create button for each of matching albums
    def populate_choose_search(self, _albums):
        _pb = []
        for count, album in enumerate(_albums):
            _pb.append(album_button(album.__str__()))
            _pb[count].clicked.connect(lambda checked, i = count: self.show_results(_albums[i]))
            self.ui.verticalLayout.addWidget(_pb[count])

        self.ui.scroll_content.setLayout(self.ui.verticalLayout)

    # clear scroll content pane upon result_page launch
    def clear_choose_content(self):
        for i in reversed(range(0, self.ui.verticalLayout.count())):
            try:
                _temp = self.ui.verticalLayout.itemAt(i).widget();
                self.ui.verticalLayout.removeWidget(_temp)
                _temp.setParent(None)
            except TypeError as e:
                print(e)

    # clear scroll content pane from playlists
    def clear_playlist_content(self):
        for i in reversed(range(0, self.ui.rmv_vertical_layout.count())):
            try:
                _temp = self.ui.rmv_vertical_layout.itemAt(i).widget();
                self.ui.rmv_vertical_layout.removeWidget(_temp)
                _temp.setParent(None)
            except TypeError as e:
                print(e)

    def show_results(self, album):
        self.handle_spotify.get_album_tracks(album)
        self.handle_spotify.get_tracks_features(album.tracks)
        _temp = self.handle_spotify.compare_album_to_top_tracks(album)
        # self.value = _temp
        _temp = (round(_temp, 2))
        _album_cover = AcquireImage(album.cover, album.name)
        _pixmap = QPixmap(get_path(album.name))
        self.ui.result_icon.setScaledContents(True)
        _pixmap.scaled(
            self.ui.result_icon.width(),
            self.ui.result_icon.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.ui.result_icon.setPixmap(_pixmap)

        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(53, 52, 60))
        # setting blur radius
        shadow.setBlurRadius(7)
        # adding shadow to the label
        self.ui.result_icon.setGraphicsEffect(shadow)

        # change page ;]
        self.ui.music_stacked.setCurrentWidget(self.ui.result_page)
        if 5 < int(_temp) <= 8:
            self.ui.result_intro.setText("not much of a difference, innit?")
        elif int(_temp) < 5:
            self.ui.result_intro.setText("worth giving it a try?")
        else:
            self.ui.result_intro.setText("basically the same features")
        self.ui.result_result.setText(
            album.__str__() + " matches your top 20 songs' features by " + str(round((_temp * 10), 2)) + "%")

        # self.ui.result_bar.setEnabled(True)
        # self._timer.timeout.connect(lambda: self.load)
        # self._timer.start(10)
        self.ui.init_error_label.setVisible(False)
        self.clear_choose_content()

    def remove_tracks_from_playlist(self, playlist, tracks):
        try:
            self.spotify.playlist_remove_all_occurences_of_items(playlist.id, tracks, snapshot_id=None)
            return True
        except:
            return False

    def remove_all_artist_tracks_from_playlist(self, playlist, artist):
        try:
            self.handle_spotify.get_playlist_tracks(playlist)
            tracks = []
            for track in playlist.tracks:
                if track.artist == artist:
                    tracks.append(track)
            if self.remove_tracks_from_playlist(playlist, tracks):
                return True, tracks
            return False
        except:
            return False

    def populate_rmv_scroll_panel(self):
        # open rmv scene
        self.ui.stackedWidget.setCurrentWidget(self.ui.rmv_page)
        # open corrent intro. rmv scene <- playlist choice
        self.ui.rmv_stacked.setCurrentWidget(self.ui.rmv_choose_playlist)

        _playlists = self.handle_spotify.get_user_playlists()
        _pb = []
        for count, playlist in enumerate(_playlists):
            _pb.append(album_button(playlist.__str__()))
            _pb[count].clicked.connect(lambda checked, i = count: self.init_rmv(_playlists[i]))

            self.ui.rmv_vertical_layout.addWidget(_pb[count])

        self.ui.rmv_scroll_content.setLayout(self.ui.verticalLayout)

    def init_rmv(self, playlist):
        # open correct scene
        self.ui.rmv_stacked.setCurrentWidget(self.ui.rmv_finalize_request)

        _playlist_cover = AcquireImage(self.spotify.playlist_cover_image(playlist.id)[0]['url'], playlist.__str__())
        _pixmap = QPixmap(get_path(playlist.__str__()))

        self.ui.rmv_playlist_icon.setScaledContents(True)

        _pixmap.scaled(
            self.ui.rmv_playlist_icon.width(),
            self.ui.rmv_playlist_icon.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.ui.rmv_playlist_icon.setPixmap(_pixmap)

        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(53, 52, 60))
        # setting blur radius
        shadow.setBlurRadius(7)
        # adding shadow to the label
        self.ui.rmv_playlist_icon.setGraphicsEffect(shadow)
        # set playlist name to title
        self.ui.rmv_playlist_label.setText(playlist.__str__())

        if self.ui.rmv_line_edit.text() != "":
            # get list of artists from query
            _artists = self.handle_spotify.search_for_artists(self.ui.rmv_line_edit.text())

            # populate dialog and open
            self.populate_dialog_content(_artists, playlist)

            #clear playlist_scroll content
            self.clear_playlist_content()
        else:
            # no text was entered prior to method call
            self.ui.rmv_line_edit.clear()
            self.ui.rmv_status_label.setStyleSheet("color: red;")
            self.ui.rmv_status_label.setText("oops, try again")

    def populate_dialog_content(self, artists, playlist):
        if artists.length() == 1:
            _results = self.remove_all_artist_tracks_from_playlist(playlist, artists[0])
            if _results[0]:
                self.ui.rmv_status_label.setStyleSheet("color: green;")
                self.ui.rmv_status_label.setText("successfully deleted "
                                                 + str(_results[1])
                                                 + " tracks by "
                                                 + artists[0]['name']
                                                 )
        else:
            _dialog = Ui_Dialog()
            _dialog.setupUi(self)

    def quit_window(self):
        self.close()

    # introduce window dragging mechanism; overriding Qt methods
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = event.pos() - self._old_pos
        self.move(self.pos() + delta)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = entWin()
    sys.exit(app.exec())
