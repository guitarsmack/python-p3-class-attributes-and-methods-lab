class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.do_all()
        
    
    def do_all(self):
        Song.add_count()
        Song.add_to_genre(self.genre)
        Song.add_to_artists(self.artist)
        Song.update_genre_count(self.genre)
        Song.updat_artist_count(self.artist)
        

    @classmethod
    def add_to_genre(cls,genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_artists(cls,artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def update_genre_count(cls,gnr):
        if gnr in cls.genre_count:
            cls.genre_count[gnr] += 1
        else:
         cls.genre_count[gnr] = 1
    
    @classmethod
    def updat_artist_count(cls,art):
        if art in cls.artist_count:
            cls.artist_count[art] += 1
        else:
            cls.artist_count[art] = 1



