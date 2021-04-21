class Track:
    def __init__(self, name, id, artist):
        self.name = name
        self.id = id
        self.artist = artist
        self.features = {}

    def create_uri(self):
        return f"spotify:track:{self.id}"

    def load_features(self, features):
        for feature in features:
            self.features[feature] = features[feature]
        return self

    def compare_tracks(self, track_to_compare):
        acousticness = 1 - abs(self.features["acousticness"] - track_to_compare.features["acousticness"])
        danceability = 1 - abs(self.features["danceability"] - track_to_compare.features["danceability"])
        energy = 1 - abs(self.features["energy"] - track_to_compare.features["energy"])
        instrumentalness = 1 - abs(self.features["instrumentalness"] - track_to_compare.features["instrumentalness"])
        liveness = 1 - abs(self.features["liveness"] - track_to_compare.features["liveness"])
        speechiness = 1 - abs(self.features["speechiness"] - track_to_compare.features["speechiness"])
        mode = 1 - abs(self.features["mode"] - track_to_compare.features["mode"])
        valence = 1 - abs(self.features["valence"] - track_to_compare.features["valence"])
        loudness = (30 - abs(self.features["loudness"] - track_to_compare.features["loudness"])) / 30
        tempo = (50 - abs(self.features["tempo"] - track_to_compare.features["tempo"])) / 50
        return acousticness + danceability + energy + instrumentalness + liveness + speechiness + mode + valence + loudness + tempo

    def __str__(self):
        for feature in self.features:
            print(feature + ": " + str(self.features[feature]))
        return "track: " + self.name + " by " + self.artist + ", id: " + self.id