import jsonpickle

# Python class representation of the Artist table in DB
class Artist:
    def __init__(self, artist_id:int,artist_name:str, genre_id:int):
        self.artist_id = artist_id
        self.ArtistName = artist_name
        self.genre_id = genre_id

    def to_json(self):
        return jsonpickle.encode(self,unpicklable=False)