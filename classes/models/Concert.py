from datetime import date
import jsonpickle

# Python class representation of the Artist table in DB
class Concert:
    def __init__(self, concert_id:int,artist_id:int, venue_id:int, tour_id:int, concert_date:date):
        self.concert_id = concert_id
        self.artist_id=artist_id
        self.venue_id=venue_id
        self.tour_id=tour_id
        self.ConcertDate=concert_date

    def to_json(self):
        return jsonpickle.encode(self,unpicklable=False)