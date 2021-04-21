import spotipy
import os


class Oauth2Manager:
    client_id = None
    client_secret = None
    client_uri = None
    is_authorized = False
    cache_handler = None

    def __init__(self):
        self.client_id = os.getenv("SPOTIPY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        self.client_uri = os.getenv("SPOTIPY_REDIRECT_URI")

    def create_spotify_oauth(self, cache_handler):
        return spotipy.SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.client_uri,
            cache_handler=cache_handler,
            scope='user-top-read \n'
                  'user-follow-read \n'
                  'user-library-read \n'
                  'playlist-modify-private\n'
                  'playlist-modify-public\n'
                  'user-read-recently-played'
            )
