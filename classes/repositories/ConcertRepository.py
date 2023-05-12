import jsonpickle
from classes.models.Concert import Concert
from classes.models.Database import Database


class ConcertRepository(Database):
    # Get a concert from the database with a given concert_id
    def get_concert_by_id(self,concert_id):
        sql = 'SELECT * FROM public."Concert" WHERE concert_id = %s;' # Note: no quotes as primary key
        data = (concert_id, )
        row = self.get_data(sql,data,True)
        print(row)
        concert = Concert(row[0],row[1],row[2],row[3],row[4])
        return concert.to_json()
    
    # Get all concerts from the database with a given artist_id
    def get_concerts_by_artist(self,artist_id):
        sql = 'SELECT * FROM public."Concert" WHERE artist_id = %s;' 
        data = (artist_id, )
        rows = self.get_data(sql,data,False)
        res = []
        for x in range(rows):
            concert = Concert(rows[x][0],rows[x][1],rows[x][2],rows[x][3],rows[x][4])
            res.append(concert)
        return jsonpickle.encode(res, False)
    
    # Get all concerts from the database with a given venue_id
    def get_concerts_by_venue(self,venue_id):
        sql = 'SELECT * FROM public."Concert" WHERE venue_id = %s;' 
        data = (venue_id, )
        rows = self.get_data(sql,data,False)
        res = []
        for x in range(rows):
            concert = Concert(rows[x][0],rows[x][1],rows[x][2],rows[x][3],rows[x][4])
            res.append(concert)
        return jsonpickle.encode(res, False)
    
     # Get all concerts from the database with a given tour_id
    def get_concerts_by_tour(self,tour_id):
        sql = 'SELECT * FROM public."Concert" WHERE tour_id = %s;' 
        data = (tour_id, )
        rows = self.get_data(sql,data,False)
        res = []
        for x in range(rows):
            concert = Concert(rows[x][0],rows[x][1],rows[x][2],rows[x][3],rows[x][4])
            res.append(concert)
        return jsonpickle.encode(res, False)