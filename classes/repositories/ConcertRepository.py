import jsonpickle
from classes.models.Concert import Concert
from classes.models.ConcertExtended import ConcertExtended
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
    
    # Get concert by concert id, joining on a varaiety of other tables to expose more data to the front end
    def get_concert_by_id_extended(self,concert_id):
        sql = """SELECT * FROM public."Concert" 
        NATURAL JOIN public."Artist" 
        NATURAL JOIN public."Genre"
        NATURAL JOIN public."Tour"
        NATURAL JOIN public."Venue"
        NATURAL JOIN public."City"
        NATURAL JOIN public."Country"
        WHERE concert_id = %s;""" # Note: no quotes as primary key
        data = (concert_id, )
        row = self.get_data(sql,data,True)
        print(row)
        concert = ConcertExtended(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13])
        return concert.to_json()
    
    def get_all_concerts_extended(self):
        sql = """SELECT * FROM public."Concert" 
        NATURAL JOIN public."Artist" 
        NATURAL JOIN public."Genre"
        NATURAL JOIN public."Tour"
        NATURAL JOIN public."Venue"
        NATURAL JOIN public."City"
        NATURAL JOIN public."Country";""" 
        data = ()
        rows = self.get_data(sql,data,False)
        res = []
        for x in range(len(rows)):
            concert = ConcertExtended(rows[x][0],rows[x][1],rows[x][2],rows[x][3],rows[x][4],rows[x][5],rows[x][6],rows[x][7],rows[x][8],rows[x][9],rows[x][10],rows[x][11],rows[x][12],rows[x][13])
            res.append(concert)
        
        return jsonpickle.encode(res, unpicklable=False)



    
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