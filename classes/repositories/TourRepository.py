from classes.models.Database import Database
from classes.models.Tour import Tour
import jsonpickle


class TourRepository(Database):
    def get_tour_by_id(self,tour_id):
        sql = 'SELECT * FROM public."Tour" WHERE tour_id = %s;' # Note: no quotes
        data = (tour_id, )
        row = self.get_data(sql,data,True)
        tour = Tour(row[0],row[1])
        return tour.to_json()
    
    def get_all_tours(self):
        sql = 'SELECT * FROM public."Tour";' # Note: no quotes
        data = ( )
        rows = self.get_data(sql,data,False)
        res = []
        for x in len(rows):
            tour = Tour(rows[x][0],rows[x][1])
            res.append(tour)
        
        return jsonpickle.encode(res,unpicklable=False)