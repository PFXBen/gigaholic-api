import jsonpickle

# Python class representation of the Artist table in DB
class ArtistExtended:
    def __init__(self, genre_id:int, artist_id:int,artist_name:str, genre_name:str):
        self.artist_id = artist_id
        self.ArtistName = artist_name
        self.genre_id = genre_id
        self.GenreName = genre_name

    def to_json(self):
        return jsonpickle.encode(self,unpicklable=False)