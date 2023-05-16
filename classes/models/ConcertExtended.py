from datetime import date
import jsonpickle

# Python class representation of the Artist table in DB
class ConcertExtended:
    def __init__(self, 
                 country_id:int, 
                 city_id:int, 
                 venue_id:int,
                 tour_id:int, 
                 genre_id:int, 
                 artist_id:int, 
                 concert_id:int,
                 concert_date:date,
                 artist_name:str,
                 genre_name:str,
                 tour_name:str,
                 venue_name:str,
                 city_name:str,
                 country_name:str):
        self.concert_id = concert_id
        self.country_id:country_id
        self.city_id:city_id
        self.genre_id:genre_id
        self.artist_id=artist_id
        self.venue_id=venue_id
        self.tour_id=tour_id
        self.ConcertDate=concert_date
        self.ArtistName=artist_name
        self.GenreName=genre_name
        self.TourName=tour_name
        self.VenueName=venue_name
        self.CityName=city_name
        self.Countryname=country_name

    def to_json(self):
        return jsonpickle.encode(self,unpicklable=False)