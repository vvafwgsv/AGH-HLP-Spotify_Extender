# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_source/final_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 700)
        mainWindow.setStyleSheet("")
        self.centralLayout = QtWidgets.QWidget(mainWindow)
        self.centralLayout.setObjectName("centralLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralLayout)
        self.mainFrame.setGeometry(QtCore.QRect(40, 30, 700, 650))
        self.mainFrame.setStyleSheet("QFrame{\n"
"    background-color: rgb(29, 29, 33);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.exitButton = QtWidgets.QPushButton(self.mainFrame)
        self.exitButton.setGeometry(QtCore.QRect(680, 7, 14, 14))
        self.exitButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 40, 54);\n"
"    border-radius: 7px;\n"
"    border: none\n"
"}")
        self.exitButton.setText("")
        self.exitButton.setCheckable(False)
        self.exitButton.setDefault(False)
        self.exitButton.setFlat(False)
        self.exitButton.setObjectName("exitButton")
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainFrame)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, 49, 701, 601))
        self.stackedWidget.setStyleSheet("QWidget{\n"
"    background-color: rgb(29, 29, 33);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.music_main_frame = QtWidgets.QFrame(self.main_page)
        self.music_main_frame.setGeometry(QtCore.QRect(0, -20, 700, 650))
        self.music_main_frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(29, 29, 33);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.music_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.music_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.music_main_frame.setObjectName("music_main_frame")
        self.welcomeLabel = QtWidgets.QLabel(self.music_main_frame)
        self.welcomeLabel.setGeometry(QtCore.QRect(310, 160, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setStyleSheet("QLabel {\n"
"    color: (255,255,255)\n"
"}")
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.widget = QtWidgets.QWidget(self.music_main_frame)
        self.widget.setGeometry(QtCore.QRect(0, 290, 701, 331))
        self.widget.setStyleSheet("QWidget {\n"
"    background-color: rgb(25, 25, 28);\n"
"}")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.music_panel = QtWidgets.QFrame(self.widget)
        self.music_panel.setMaximumSize(QtCore.QSize(150, 200))
        self.music_panel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.music_panel.setStyleSheet("QFrame#music_panel{\n"
"    border-radius: 15px;\n"
"    background-color: rgb(52, 52, 60);\n"
"}")
        self.music_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.music_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.music_panel.setObjectName("music_panel")
        self.sec_music_label = QtWidgets.QLabel(self.music_panel)
        self.sec_music_label.setGeometry(QtCore.QRect(20, 160, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.sec_music_label.setFont(font)
        self.sec_music_label.setStyleSheet("QLabel {\n"
"    color: (255,255,255);\n"
"    background-color: rgb(52, 52, 60);\n"
"}\n"
"")
        self.sec_music_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.sec_music_label.setObjectName("sec_music_label")
        self.music_icon = QtWidgets.QLabel(self.music_panel)
        self.music_icon.setGeometry(QtCore.QRect(14, 10, 120, 120))
        self.music_icon.setStyleSheet("QLabel {\n"
"    border:none;\n"
"    border-radius: 60;\n"
"\n"
"}")
        self.music_icon.setText("")
        self.music_icon.setObjectName("music_icon")
        self.main_music_label = QtWidgets.QLabel(self.music_panel)
        self.main_music_label.setGeometry(QtCore.QRect(20, 140, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.main_music_label.setFont(font)
        self.main_music_label.setStyleSheet("QLabel {\n"
"    color: (255,255,255);\n"
"    background-color: rgb(52, 52, 60);\n"
"}\n"
"")
        self.main_music_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.main_music_label.setObjectName("main_music_label")
        self.music_btn = QtWidgets.QPushButton(self.music_panel)
        self.music_btn.setGeometry(QtCore.QRect(90, 80, 50, 50))
        self.music_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 25px;\n"
"    border: none;\n"
"    background-color: rgb(67, 168, 63);\n"
"}")
        self.music_btn.setText("")
        self.music_btn.setObjectName("music_btn")
        self.horizontalLayout.addWidget(self.music_panel)
        self.rmv_panel = QtWidgets.QFrame(self.widget)
        self.rmv_panel.setMaximumSize(QtCore.QSize(150, 200))
        self.rmv_panel.setStyleSheet("QFrame#rmv_panel{\n"
"    border-radius: 15px;\n"
"    background-color: rgb(52, 52, 60);\n"
"}")
        self.rmv_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rmv_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rmv_panel.setObjectName("rmv_panel")
        self.rmv_icon = QtWidgets.QLabel(self.rmv_panel)
        self.rmv_icon.setGeometry(QtCore.QRect(14, 10, 120, 120))
        self.rmv_icon.setStyleSheet("QLabel {\n"
"    border:none;\n"
"    border-radius: 60;\n"
"\n"
"}")
        self.rmv_icon.setText("")
        self.rmv_icon.setObjectName("rmv_icon")
        self.main_rmv_label = QtWidgets.QLabel(self.rmv_panel)
        self.main_rmv_label.setGeometry(QtCore.QRect(20, 140, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.main_rmv_label.setFont(font)
        self.main_rmv_label.setStyleSheet("QLabel {\n"
"    color: (255,255,255);\n"
"    background-color: rgb(52, 52, 60);\n"
"}\n"
"")
        self.main_rmv_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.main_rmv_label.setObjectName("main_rmv_label")
        self.sec_rmv_label = QtWidgets.QLabel(self.rmv_panel)
        self.sec_rmv_label.setGeometry(QtCore.QRect(20, 160, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.sec_rmv_label.setFont(font)
        self.sec_rmv_label.setStyleSheet("QLabel {\n"
"    color: (255,255,255);\n"
"    background-color: rgb(52, 52, 60);\n"
"}\n"
"")
        self.sec_rmv_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.sec_rmv_label.setObjectName("sec_rmv_label")
        self.rmv_btn = QtWidgets.QPushButton(self.rmv_panel)
        self.rmv_btn.setGeometry(QtCore.QRect(90, 80, 50, 50))
        self.rmv_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 25px;\n"
"    border: none;\n"
"    background-color: rgb(67, 168, 63);\n"
"}")
        self.rmv_btn.setText("")
        self.rmv_btn.setObjectName("rmv_btn")
        self.horizontalLayout.addWidget(self.rmv_panel)
        self.avatar = QtWidgets.QLabel(self.music_main_frame)
        self.avatar.setGeometry(QtCore.QRect(70, 70, 200, 200))
        self.avatar.setStyleSheet("QLabel {\n"
"    \n"
"    background-color: rgb(52, 52, 60);\n"
"    border-radius:100px;\n"
"}")
        self.avatar.setText("")
        self.avatar.setObjectName("avatar")
        self.thefuck = QtWidgets.QLabel(self.music_main_frame)
        self.thefuck.setGeometry(QtCore.QRect(280, 220, 361, 31))
        self.thefuck.setObjectName("thefuck")
        self.stackedWidget.addWidget(self.main_page)
        self.music_page = QtWidgets.QWidget()
        self.music_page.setObjectName("music_page")
        self.music_page_main_frame = QtWidgets.QFrame(self.music_page)
        self.music_page_main_frame.setGeometry(QtCore.QRect(110, 60, 481, 441))
        self.music_page_main_frame.setStyleSheet("QFrame {\n"
"    border-radius: 15px;\n"
"    color: rgb(196, 196, 196);\n"
"    background-color: rgb(61, 61, 70);\n"
"}")
        self.music_page_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.music_page_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.music_page_main_frame.setObjectName("music_page_main_frame")
        self.exit_music = QtWidgets.QPushButton(self.music_page_main_frame)
        self.exit_music.setGeometry(QtCore.QRect(460, 10, 14, 14))
        self.exit_music.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 40, 54);\n"
"    border-radius: 7px;\n"
"    border: none\n"
"}")
        self.exit_music.setText("")
        self.exit_music.setCheckable(False)
        self.exit_music.setDefault(False)
        self.exit_music.setFlat(False)
        self.exit_music.setObjectName("exit_music")
        self.music_stacked = QtWidgets.QStackedWidget(self.music_page_main_frame)
        self.music_stacked.setGeometry(QtCore.QRect(0, 30, 481, 411))
        self.music_stacked.setStyleSheet("QWidget {\n"
"    border-radius: 15px;\n"
"    color: rgb(196, 196, 196);\n"
"    background-color: rgb(61, 61, 70);\n"
"}")
        self.music_stacked.setObjectName("music_stacked")
        self.init_search_page = QtWidgets.QWidget()
        self.init_search_page.setObjectName("init_search_page")
        self.init_search_frame = QtWidgets.QFrame(self.init_search_page)
        self.init_search_frame.setGeometry(QtCore.QRect(69, 39, 351, 331))
        self.init_search_frame.setStyleSheet("QFrame{\n"
"    border-radius:15px;\n"
"    background-color: rgb(70, 69, 80);\n"
"    color:rbg(255,255,255)\n"
"}")
        self.init_search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.init_search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.init_search_frame.setObjectName("init_search_frame")
        self.init_search_welcome_label = QtWidgets.QLabel(self.init_search_frame)
        self.init_search_welcome_label.setGeometry(QtCore.QRect(40, 30, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.init_search_welcome_label.setFont(font)
        self.init_search_welcome_label.setStyleSheet("QLabel{\n"
"    border-radius:10px;\n"
"    \n"
"    background-color: rgba(69, 68, 79, 189);\n"
"}")
        self.init_search_welcome_label.setWordWrap(True)
        self.init_search_welcome_label.setObjectName("init_search_welcome_label")
        self.init_line_edit = QtWidgets.QLineEdit(self.init_search_frame)
        self.init_line_edit.setGeometry(QtCore.QRect(40, 100, 231, 31))
        self.init_line_edit.setStyleSheet("QLineEdit{\n"
"    color:rgb(255,255,255);\n"
"}")
        self.init_line_edit.setClearButtonEnabled(False)
        self.init_line_edit.setObjectName("init_line_edit")
        self.init_error_label = QtWidgets.QLabel(self.init_search_frame)
        self.init_error_label.setGeometry(QtCore.QRect(40, 150, 181, 51))
        self.init_error_label.setStyleSheet("QLabel{\n"
"    color: rgb(239, 45, 26);\n"
"}")
        self.init_error_label.setScaledContents(False)
        self.init_error_label.setObjectName("init_error_label")
        self.init_search = QtWidgets.QPushButton(self.init_search_frame)
        self.init_search.setGeometry(QtCore.QRect(285, 108, 14, 14))
        self.init_search.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(134, 255, 100);\n"
"    border-radius: 7px;\n"
"    border: none\n"
"}")
        self.init_search.setText("")
        self.init_search.setCheckable(False)
        self.init_search.setDefault(False)
        self.init_search.setFlat(False)
        self.init_search.setObjectName("init_search")
        self.music_stacked.addWidget(self.init_search_page)
        self.choose_search = QtWidgets.QWidget()
        self.choose_search.setObjectName("choose_search")
        self.choose_frame = QtWidgets.QFrame(self.choose_search)
        self.choose_frame.setGeometry(QtCore.QRect(69, 39, 351, 331))
        self.choose_frame.setStyleSheet("QFrame{\n"
"    border-radius:15px;\n"
"    \n"
"background-color:rgb(61, 61, 70);\n"
"}")
        self.choose_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.choose_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.choose_frame.setObjectName("choose_frame")
        self.exit_choose = QtWidgets.QPushButton(self.choose_frame)
        self.exit_choose.setGeometry(QtCore.QRect(280, 300, 61, 20))
        self.exit_choose.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(133, 255, 120);\n"
"    border-radius: 7px;\n"
"    border: none\n"
"}\n"
"QPushButton:pressed{\n"
"    color: black;\n"
"    background-color: rgb(109, 207, 97);\n"
"    border-radius: 7px;\n"
"    border: none\n"
"}")
        self.exit_choose.setCheckable(False)
        self.exit_choose.setDefault(False)
        self.exit_choose.setFlat(False)
        self.exit_choose.setObjectName("exit_choose")
        self.choose_label = QtWidgets.QLabel(self.choose_frame)
        self.choose_label.setGeometry(QtCore.QRect(0, 0, 111, 48))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.choose_label.setFont(font)
        self.choose_label.setStyleSheet("QLabel{\n"
"    border-radius:10px;\n"
"    color:rbg(255,255,255);\n"
"    background-color: rgb(61, 61, 70);\n"
"\n"
"}")
        self.choose_label.setObjectName("choose_label")
        self.scrollArea = QtWidgets.QScrollArea(self.choose_frame)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 341, 201))
        self.scrollArea.setStyleSheet("QScrollBar:vertical {\n"
"            border: 0px solid #999999;\n"
"        \n"
"        background-color: rgb(61, 61, 70);\n"
"            width:8px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 10px;\n"
"              border: 0px solid red;\n"
"            border-radius: 4px;\n"
"        \n"
"    background-color: rgb(36, 35, 41);\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scroll_content = QtWidgets.QWidget()
        self.scroll_content.setGeometry(QtCore.QRect(0, 0, 320, 201))
        self.scroll_content.setMaximumSize(QtCore.QSize(320, 16777215))
        self.scroll_content.setObjectName("scroll_content")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scroll_content)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 311, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scroll_content)
        self.music_stacked.addWidget(self.choose_search)
        self.result_page = QtWidgets.QWidget()
        self.result_page.setObjectName("result_page")
        self.result_frame = QtWidgets.QFrame(self.result_page)
        self.result_frame.setGeometry(QtCore.QRect(30, 30, 421, 341))
        self.result_frame.setStyleSheet("QFrame{\n"
"    border-radius:15px;\n"
"    \n"
"    background-color: rgb(61, 61, 70);\n"
"    \n"
"}")
        self.result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_frame.setObjectName("result_frame")
        self.reload_result = QtWidgets.QPushButton(self.result_frame)
        self.reload_result.setGeometry(QtCore.QRect(170, 300, 91, 20))
        self.reload_result.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(133, 255, 120);\n"
"    border-radius: 7px;\n"
"    border: none\n"
"}\n"
"QPushButton:pressed{\n"
"    color: black;\n"
"    background-color: rgb(109, 207, 97);\n"
"    border-radius: 7px;\n"
"    border: none\n"
"}")
        self.reload_result.setCheckable(False)
        self.reload_result.setDefault(False)
        self.reload_result.setFlat(False)
        self.reload_result.setObjectName("reload_result")
        self.result_intro = QtWidgets.QLabel(self.result_frame)
        self.result_intro.setGeometry(QtCore.QRect(20, 180, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.result_intro.setFont(font)
        self.result_intro.setStyleSheet("QLabel{\n"
"    color:rgb(255,255,255)\n"
"}")
        self.result_intro.setObjectName("result_intro")
        self.result_result = QtWidgets.QLabel(self.result_frame)
        self.result_result.setGeometry(QtCore.QRect(20, 230, 401, 48))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        self.result_result.setFont(font)
        self.result_result.setStyleSheet("QLabel{\n"
"    color:rgb(255,255,255)\n"
"}")
        self.result_result.setWordWrap(True)
        self.result_result.setObjectName("result_result")
        self.result_icon = QtWidgets.QLabel(self.result_frame)
        self.result_icon.setGeometry(QtCore.QRect(25, 0, 160, 160))
        self.result_icon.setStyleSheet("QLabel {\n"
"    border: 2px;\n"
"    border-color: black;\n"
"}")
        self.result_icon.setText("")
        self.result_icon.setObjectName("result_icon")
        self.music_stacked.addWidget(self.result_page)
        self.stackedWidget.addWidget(self.music_page)
        self.rmv_page = QtWidgets.QWidget()
        self.rmv_page.setObjectName("rmv_page")
        self.rmv_page_main_frame = QtWidgets.QFrame(self.rmv_page)
        self.rmv_page_main_frame.setGeometry(QtCore.QRect(110, 60, 481, 441))
        self.rmv_page_main_frame.setStyleSheet("QFrame {\n"
"    border-radius: 15px;\n"
"    color: rgb(196, 196, 196);\n"
"    background-color: rgb(61, 61, 70);\n"
"}")
        self.rmv_page_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rmv_page_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rmv_page_main_frame.setObjectName("rmv_page_main_frame")
        self.exit_rmv = QtWidgets.QPushButton(self.rmv_page_main_frame)
        self.exit_rmv.setGeometry(QtCore.QRect(460, 10, 14, 14))
        self.exit_rmv.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 40, 54);\n"
"    border-radius: 7px;\n"
"    border: none\n"
"}")
        self.exit_rmv.setText("")
        self.exit_rmv.setCheckable(False)
        self.exit_rmv.setDefault(False)
        self.exit_rmv.setFlat(False)
        self.exit_rmv.setObjectName("exit_rmv")
        self.rmv_stacked = QtWidgets.QStackedWidget(self.rmv_page_main_frame)
        self.rmv_stacked.setGeometry(QtCore.QRect(20, 50, 441, 371))
        self.rmv_stacked.setStyleSheet("QWidget{\n"
"    background-color: rgb(61, 61, 70);\n"
"}")
        self.rmv_stacked.setObjectName("rmv_stacked")
        self.rmv_choose_playlist = QtWidgets.QWidget()
        self.rmv_choose_playlist.setStyleSheet("QWidget{\n"
"    background-color: rgb(61, 61, 70);\n"
"}")
        self.rmv_choose_playlist.setObjectName("rmv_choose_playlist")
        self.rmv_choose_frame = QtWidgets.QFrame(self.rmv_choose_playlist)
        self.rmv_choose_frame.setGeometry(QtCore.QRect(50, 20, 351, 331))
        self.rmv_choose_frame.setStyleSheet("QFrame{\n"
"    border-radius:15px;\n"
"    \n"
"background-color:rgb(61, 61, 70);\n"
"}")
        self.rmv_choose_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rmv_choose_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rmv_choose_frame.setObjectName("rmv_choose_frame")
        self.rmv_exit_playlist = QtWidgets.QPushButton(self.rmv_choose_frame)
        self.rmv_exit_playlist.setGeometry(QtCore.QRect(280, 300, 61, 20))
        self.rmv_exit_playlist.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(133, 255, 120);\n"
"    border-radius: 7px;\n"
"    border: none\n"
"}\n"
"QPushButton:pressed{\n"
"    color: black;\n"
"    background-color: rgb(109, 207, 97);\n"
"    border-radius: 7px;\n"
"    border: none\n"
"}")
        self.rmv_exit_playlist.setCheckable(False)
        self.rmv_exit_playlist.setDefault(False)
        self.rmv_exit_playlist.setFlat(False)
        self.rmv_exit_playlist.setObjectName("rmv_exit_playlist")
        self.rmv_playlist_scroll = QtWidgets.QScrollArea(self.rmv_choose_frame)
        self.rmv_playlist_scroll.setGeometry(QtCore.QRect(0, 60, 341, 201))
        self.rmv_playlist_scroll.setStyleSheet("QScrollBar:vertical {\n"
"            border: 0px solid #999999;\n"
"        \n"
"        background-color: rgb(61, 61, 70);\n"
"            width:8px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 10px;\n"
"              border: 0px solid red;\n"
"            border-radius: 4px;\n"
"        \n"
"    background-color: rgb(36, 35, 41);\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.rmv_playlist_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.rmv_playlist_scroll.setWidgetResizable(True)
        self.rmv_playlist_scroll.setObjectName("rmv_playlist_scroll")
        self.rmv_playlist_scroll_content = QtWidgets.QWidget()
        self.rmv_playlist_scroll_content.setGeometry(QtCore.QRect(0, 0, 320, 201))
        self.rmv_playlist_scroll_content.setMaximumSize(QtCore.QSize(320, 16777215))
        self.rmv_playlist_scroll_content.setObjectName("rmv_playlist_scroll_content")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.rmv_playlist_scroll_content)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 311, 201))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.rmv_playlist_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.rmv_playlist_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.rmv_playlist_layout.setContentsMargins(1, 1, 1, 1)
        self.rmv_playlist_layout.setSpacing(5)
        self.rmv_playlist_layout.setObjectName("rmv_playlist_layout")
        self.rmv_playlist_scroll.setWidget(self.rmv_playlist_scroll_content)
        self.rmv_choose_label = QtWidgets.QLabel(self.rmv_choose_frame)
        self.rmv_choose_label.setGeometry(QtCore.QRect(0, 10, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.rmv_choose_label.setFont(font)
        self.rmv_choose_label.setStyleSheet("QLabel{\n"
"    color: white;\n"
"\n"
"}")
        self.rmv_choose_label.setObjectName("rmv_choose_label")
        self.rmv_stacked.addWidget(self.rmv_choose_playlist)
        self.rmv_finalize_request = QtWidgets.QWidget()
        self.rmv_finalize_request.setObjectName("rmv_finalize_request")
        self.rmv_playlist_icon = QtWidgets.QLabel(self.rmv_finalize_request)
        self.rmv_playlist_icon.setGeometry(QtCore.QRect(20, 10, 150, 150))
        self.rmv_playlist_icon.setText("")
        self.rmv_playlist_icon.setObjectName("rmv_playlist_icon")
        self.rmv_final_label = QtWidgets.QLabel(self.rmv_finalize_request)
        self.rmv_final_label.setGeometry(QtCore.QRect(30, 180, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.rmv_final_label.setFont(font)
        self.rmv_final_label.setStyleSheet("QLabel {\n"
"    color:white;\n"
"}")
        self.rmv_final_label.setObjectName("rmv_final_label")
        self.rmv_line_edit = QtWidgets.QLineEdit(self.rmv_finalize_request)
        self.rmv_line_edit.setGeometry(QtCore.QRect(110, 230, 221, 31))
        self.rmv_line_edit.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(29, 29, 33);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.rmv_line_edit.setObjectName("rmv_line_edit")
        self.rmv_init_btn = QtWidgets.QPushButton(self.rmv_finalize_request)
        self.rmv_init_btn.setGeometry(QtCore.QRect(150, 280, 141, 21))
        self.rmv_init_btn.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(133, 255, 120);\n"
"    border-radius: 7px;\n"
"    border: none\n"
"}\n"
"QPushButton:pressed{\n"
"    color: black;\n"
"    background-color: rgb(109, 207, 97);\n"
"    border-radius: 7px;\n"
"    border: none\n"
"}")
        self.rmv_init_btn.setCheckable(False)
        self.rmv_init_btn.setDefault(False)
        self.rmv_init_btn.setFlat(False)
        self.rmv_init_btn.setObjectName("rmv_init_btn")
        self.rmv_playlist_label = QtWidgets.QLabel(self.rmv_finalize_request)
        self.rmv_playlist_label.setGeometry(QtCore.QRect(190, 30, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.rmv_playlist_label.setFont(font)
        self.rmv_playlist_label.setStyleSheet("QLabel {\n"
"    color:white;\n"
"}")
        self.rmv_playlist_label.setObjectName("rmv_playlist_label")
        self.rmv_status_label = QtWidgets.QLabel(self.rmv_finalize_request)
        self.rmv_status_label.setGeometry(QtCore.QRect(190, 100, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.rmv_status_label.setFont(font)
        self.rmv_status_label.setStyleSheet("QLabel {\n"
"    color:white;\n"
"}")
        self.rmv_status_label.setWordWrap(True)
        self.rmv_status_label.setObjectName("rmv_status_label")
        self.rmv_stacked.addWidget(self.rmv_finalize_request)
        self.rmv_specify_artist = QtWidgets.QWidget()
        self.rmv_specify_artist.setObjectName("rmv_specify_artist")
        self.rmv_specify_frame = QtWidgets.QFrame(self.rmv_specify_artist)
        self.rmv_specify_frame.setGeometry(QtCore.QRect(50, 20, 351, 331))
        self.rmv_specify_frame.setStyleSheet("QFrame{\n"
"    border-radius:15px;\n"
"    \n"
"background-color:rgb(61, 61, 70);\n"
"}")
        self.rmv_specify_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rmv_specify_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rmv_specify_frame.setObjectName("rmv_specify_frame")
        self.rmv_exit_specify = QtWidgets.QPushButton(self.rmv_specify_frame)
        self.rmv_exit_specify.setGeometry(QtCore.QRect(280, 300, 61, 20))
        self.rmv_exit_specify.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: rgb(133, 255, 120);\n"
"    border-radius: 7px;\n"
"    border: none\n"
"}\n"
"QPushButton:pressed{\n"
"    color: black;\n"
"    background-color: rgb(109, 207, 97);\n"
"    border-radius: 7px;\n"
"    border: none\n"
"}")
        self.rmv_exit_specify.setCheckable(False)
        self.rmv_exit_specify.setDefault(False)
        self.rmv_exit_specify.setFlat(False)
        self.rmv_exit_specify.setObjectName("rmv_exit_specify")
        self.rmv_specify_scroll = QtWidgets.QScrollArea(self.rmv_specify_frame)
        self.rmv_specify_scroll.setGeometry(QtCore.QRect(0, 60, 341, 201))
        self.rmv_specify_scroll.setStyleSheet("QScrollBar:vertical {\n"
"            border: 0px solid #999999;\n"
"        \n"
"        background-color: rgb(61, 61, 70);\n"
"            width:8px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 10px;\n"
"              border: 0px solid red;\n"
"            border-radius: 4px;\n"
"        \n"
"    background-color: rgb(36, 35, 41);\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.rmv_specify_scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.rmv_specify_scroll.setWidgetResizable(True)
        self.rmv_specify_scroll.setObjectName("rmv_specify_scroll")
        self.rmv_specify_scroll_content = QtWidgets.QWidget()
        self.rmv_specify_scroll_content.setGeometry(QtCore.QRect(0, 0, 320, 201))
        self.rmv_specify_scroll_content.setMaximumSize(QtCore.QSize(320, 16777215))
        self.rmv_specify_scroll_content.setStyleSheet("QScrollBar:vertical {\n"
"            border: 0px solid #999999;\n"
"        \n"
"        background-color: rgb(61, 61, 70);\n"
"            width:8px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 10px;\n"
"              border: 0px solid red;\n"
"            border-radius: 4px;\n"
"        \n"
"    background-color: rgb(36, 35, 41);\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.rmv_specify_scroll_content.setObjectName("rmv_specify_scroll_content")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.rmv_specify_scroll_content)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 311, 201))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.rmv_specify_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.rmv_specify_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.rmv_specify_layout.setContentsMargins(1, 1, 1, 1)
        self.rmv_specify_layout.setSpacing(5)
        self.rmv_specify_layout.setObjectName("rmv_specify_layout")
        self.rmv_specify_scroll.setWidget(self.rmv_specify_scroll_content)
        self.rmv_specify_label = QtWidgets.QLabel(self.rmv_specify_frame)
        self.rmv_specify_label.setGeometry(QtCore.QRect(0, 10, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.rmv_specify_label.setFont(font)
        self.rmv_specify_label.setStyleSheet("QLabel{\n"
"    color: white;\n"
"\n"
"}")
        self.rmv_specify_label.setObjectName("rmv_specify_label")
        self.rmv_stacked.addWidget(self.rmv_specify_artist)
        self.stackedWidget.addWidget(self.rmv_page)
        mainWindow.setCentralWidget(self.centralLayout)

        self.retranslateUi(mainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.music_stacked.setCurrentIndex(2)
        self.rmv_stacked.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.welcomeLabel.setText(_translate("mainWindow", "NAME"))
        self.sec_music_label.setText(_translate("mainWindow", "some tunes"))
        self.main_music_label.setText(_translate("mainWindow", "compare"))
        self.main_rmv_label.setText(_translate("mainWindow", "remove"))
        self.sec_rmv_label.setText(_translate("mainWindow", "some thrash"))
        self.thefuck.setText(_translate("mainWindow", "PUB PLAY * FOLLOWERS * FOLLOWING"))
        self.init_search_welcome_label.setText(_translate("mainWindow", "<html><head/><body><p>Choose album</p><p>to match with your top 20 songs</p></body></html>"))
        self.init_error_label.setText(_translate("mainWindow", "Oops, we didn\'t find that. \n"
"Try again!"))
        self.exit_choose.setText(_translate("mainWindow", "quit"))
        self.choose_label.setText(_translate("mainWindow", "Which one?"))
        self.reload_result.setText(_translate("mainWindow", "try again!"))
        self.result_intro.setText(_translate("mainWindow", "placeholder"))
        self.result_result.setText(_translate("mainWindow", "placeholder"))
        self.rmv_exit_playlist.setText(_translate("mainWindow", "quit"))
        self.rmv_choose_label.setText(_translate("mainWindow", "choose playlist to edit"))
        self.rmv_final_label.setText(_translate("mainWindow", "hmm, who\'s pain in the ass?"))
        self.rmv_init_btn.setText(_translate("mainWindow", "make them go!"))
        self.rmv_playlist_label.setText(_translate("mainWindow", "TextLabel"))
        self.rmv_status_label.setText(_translate("mainWindow", "TextLabel"))
        self.rmv_exit_specify.setText(_translate("mainWindow", "quit"))
        self.rmv_specify_label.setText(_translate("mainWindow", "hmmm, which one?"))
