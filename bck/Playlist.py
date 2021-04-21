class Playlist:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tracks = []
        self.features = {}

    def load_tracks(self, tracks):
        for track in tracks:
            self.tracks.append(track)
        return self

    def __str__(self):
        return self.name