
class Album:
    def __init__(self, name, id, artist, cover):
        self.name = name
        self.id = id
        self.artist = artist
        self.tracks = []
        self.features = {}
        self.cover = cover

    def load_tracks(self, tracks):
        for track in tracks:
            self.tracks.append(track)
        return self

    def calculate_album_features(self):
        for feature in self.tracks[0].features:
            self.features[feature] = 0
            for track in self.tracks:
                try:
                    self.features[feature] = self.features[feature] + float(track.features[feature])
                except: pass
            self.features[feature] /= len(self.tracks)

    def compare_albums(self, album_to_compare):
        self.calculate_album_features()
        album_to_compare.calculate_album_features()
        acousticness = 1 - abs(self.features["acousticness"] - album_to_compare.features["acousticness"])
        danceability = 1 - abs(self.features["danceability"] - album_to_compare.features["danceability"])
        energy = 1 - abs(self.features["energy"] - album_to_compare.features["energy"])
        instrumentalness = 1 - abs(self.features["instrumentalness"] - album_to_compare.features["instrumentalness"])
        liveness = 1 - abs(self.features["liveness"] - album_to_compare.features["liveness"])
        speechiness = 1 - abs(self.features["speechiness"] - album_to_compare.features["speechiness"])
        mode = 1 - abs(self.features["mode"] - album_to_compare.features["mode"])
        valence = 1 - abs(self.features["valence"] - album_to_compare.features["valence"])
        loudness = (30 - abs(self.features["loudness"] - album_to_compare.features["loudness"])) / 30
        tempo = (50 - abs(self.features["tempo"] - album_to_compare.features["tempo"])) / 50
        return ((acousticness + danceability + energy + instrumentalness + liveness + speechiness + mode + valence + loudness + tempo)**2)/10

    def check_album_diversity(self):
        diversity = 0
        for i, track in enumerate(self.tracks):
            for track_to_compare in self.tracks:
                diversity += track.compare_tracks(track_to_compare)
        diversity /= (len(self.tracks) ** 2)
        return diversity

    def __str__(self):
        return self.name + " by " + self.artist
