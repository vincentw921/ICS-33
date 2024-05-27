class Album:
    _songs = []

    def __init__(self, artist):
        self._artist = artist
        Album._songs = []

    def artist(self):
        return self._artist

    def songs(self):
        return self._songs

    def add_song(self, song):
        self._songs.append(song)
        
a1 = Album("me")
a1.add_song("hello world")
a1.add_song("i love you")

a2 = Album("you")

print(a1.songs())