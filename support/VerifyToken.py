from spotipy import cache_handler, oauth2

class VerifyToken:
    cache_handler = None
    auth_manager = None
    is_valid = False

    def __init__(self, session_cache_path):
        self.cache_handler = cache_handler.CacheFileHandler(cache_path=session_cache_path)
        self.auth_manager = oauth2.SpotifyOAuth(cache_handler=self.cache_handler)
        if self.auth_manager.validate_token(self.cache_handler.get_cached_token()):
            self.is_valid = True

    def refresh_token(self):
        if self.auth_manager.is_token_expired(self.cache_handler.get_cached_token()):
            self.auth_manager.refresh_access_token(self.cache_handler.get_cached_token())

    def get_status(self):
        return self.is_valid
