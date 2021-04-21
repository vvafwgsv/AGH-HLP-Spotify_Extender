import json

import requests

from bck.Album import Album
from bck.Artist import Artist
from bck.Playlist import Playlist
from bck.Track import Track


class SpotifyClient:
    def __init__(self, access_token, user_id):
        self.access_token = access_token
        self.user_id = user_id

    def get_user_id(self):
        response = requests.get(
            'https://api.spotify.com/v1/me',
            headers={
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        return response.json()["id"]

    def search_for_track(self, name, artist):
        try:
            response = requests.get(
                f'https://api.spotify.com/v1/search?q={artist}%20{name}&type=track&',
                headers={
                    "Authorization": f"Bearer {self.access_token}"
                }
            )
            tracks = [Track(track["name"], track["id"], track["artists"][0]["name"]) for track in response.json()["tracks"]["items"]]
            return tracks
        except: return False

    def search_for_album(self, name, artist):
        try:
            response = requests.get(
                f'https://api.spotify.com/v1/search?q={artist}%20{name}&type=album&',
                headers={
                    "Authorization": f"Bearer {self.access_token}"
                }
            )
            album = [Album(album["name"], album["id"], album["artists"][0]["name"], album["images"][0]["url"]) for album in response.json()['albums']["items"]]
            return album
        except: return False

    def get_current_track(self):
        response = requests.get(
            'https://api.spotify.com/v1/me/player/currently-playing',
            headers={
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        name = response.json()["item"]["name"]
        id = response.json()["item"]["id"]
        artists = [artist for artist in response.json()['item']['artists']]
        artist_names = ', '.join([artist['name'] for artist in artists])
        current_track = Track(name, id, artist_names)
        features = self.get_track_features(current_track)
        current_track.load_features(features)
        return current_track

    def get_track_features(self, track):
        response = requests.get(
            f'https://api.spotify.com/v1/audio-features/{track.id}',
            headers={
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        track.load_features(response.json())
        return track

    def get_tracks_features(self, tracks):
        ids = "ids="
        for track in tracks:
            ids = ids + track.id + "%2C"
        response = requests.get(
            f'https://api.spotify.com/v1/audio-features/?{ids}',
            headers={
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        for count, track in enumerate(tracks):
            track.load_features(response.json()["audio_features"][count])
        return tracks

    def get_recently_played(self, limit):
        response = requests.get(
            f'	https://api.spotify.com/v1/me/player/recently-played?limit={limit}',
            headers={
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for track in
                  response.json()["items"]]
        return tracks

    def get_user_playlists(self):
        response = requests.get(
            f'	https://api.spotify.com/v1/users/{self.user_id}/playlists',
            headers={
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        playlists = [Playlist(playlist["name"], playlist["id"]) for playlist in response.json()["items"]]
        for playlist in playlists:
            self.get_playlist_tracks(playlist)
        return playlists

    def get_playlist_tracks(self, playlist):
        response = requests.get(
            f'https://api.spotify.com/v1/playlists/{playlist.id}/tracks',
            headers={
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for track in
                  response.json()["items"]]
        return playlist.load_tracks(tracks)

    def create_playlist(self, name, description, is_public):
        response = requests.post(
            f"https://api.spotify.com/v1/users/{self.user_id}/playlists",
            data=json.dumps({
                "name": name,
                "description": description,
                "public": is_public
            }),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        playlist_id = response.json()["id"]
        playlist = Playlist(name, playlist_id)
        return playlist

    def add_to_playlist(self, playlist, tracks):
        tracks_uri = [track.create_uri() for track in tracks]
        response = requests.post(
            f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks",
            data=json.dumps(tracks_uri),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        return playlist

    def remove_starlings(self):
        playlists = self.get_user_playlists()
        for playlist in playlists:
            for position, track in enumerate(playlist.tracks):
                if track.artist == "Szpaku":
                    uri = track.create_uri
                    response = requests.delete(
                        f'https://api.spotify.com/v1/playlists/{playlist.id}/tracks',
                        data=json.dumps({
                            "uri": uri,
                            "positions": position,
                        }),
                        headers={
                            "Authorization": f"Bearer {self.access_token}"
                        }
                    )
        return "Usunięto wszystkie tracki szpaka z playlist"

    def get_album_tracks(self, album):
        response = requests.get(
            f'https://api.spotify.com/v1/albums/{album.id}/tracks',
            headers={
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        tracks = [Track(track["name"], track["id"], track["artists"][0]["name"]) for track in
                  response.json()["items"]]
        return album.load_tracks(tracks)

    def get_top_tracks(self):
        response = requests.get(
            f'https://api.spotify.com/v1/me/top/tracks?limit=20',
            headers={
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        tracks = [Track(track["name"], track["id"], track["album"]["artists"][0]["name"]) for track in
                  response.json()["items"]]
        return tracks

    def compare_album_to_top_tracks(self, album):
        my_album = Album("My top tracks", False, False, False)
        my_album.load_tracks(self.get_top_tracks())
        self.get_tracks_features(my_album.tracks)
        return my_album.compare_albums(album)

    def get_recommendations(self, tracks, limit = 20):
        ids = "seed_tracks="
        for track in tracks:
            ids = ids + track.id + "%2C"
        response = requests.get(
            f'https://api.spotify.com/v1/recommendations?limit={limit}&{ids}',
            headers={
                "Authorization": f"Bearer {self.access_token}"
            }
        )
        recommended_tracks = [Track(recommended_track["name"], recommended_track["id"], recommended_track["artists"][0]["name"]) for recommended_track in
                  response.json()["tracks"]]
        return recommended_tracks

    def search_for_artist(self, artist, limit=10):
        try:
            response = requests.get(
                f'https://api.spotify.com/v1/search?q={artist}&type=artist&limit={limit}&',
                headers={
                    "Authorization": f"Bearer {self.access_token}"
                }
            )
            artists = [Artist(artist["name"], artist["id"]) for artist in response.json()['artists']["items"]]
            return artists
        except: return False