import jsonpickle
from classes.models.Artist import Artist
from classes.models.Database import Database


class ArtistRepository(Database):
    # Get an artist from the database with a given artist_id
    def get_artist_by_id(self, artist_id:int):
        sql = 'SELECT * FROM public."Artist" WHERE artist_id = %s;' # Note: no quotes
        data = (artist_id, )
        row = self.get_data(sql,data,True)
        user = Artist(row[0],row[1],row[2])
        return user.to_json()
    
    # Get all artists with a given genre_id
    def get_artists_by_genre_id(self, genre_id:int):
        sql = 'SELECT * FROM public."Artist" WHERE "genre_id" = %s;' # Note: no quotes
        data = (genre_id, )
        rows = self.get_data(sql,data,False)
        res = []
        for x in range(len(rows)):
            artist = Artist(rows[x][0],rows[x][1],rows[x][2])
            res.append(artist)
        return jsonpickle.encode(res, False)
    
    # Get all artists in the database
    def get_all_artists(self):
        sql = 'SELECT * FROM public."Artist";' # Note: no quotes
        data = ()
        rows = self.get_data(sql,data,False)
        res = []
        for x in range(len(rows)):
            artist = Artist(rows[x][0],rows[x][1],rows[x][2])
            res.append(artist)
        return jsonpickle.encode(res, False)