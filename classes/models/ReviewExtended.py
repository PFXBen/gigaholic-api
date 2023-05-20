# Python class representation of the Review table in DB
import datetime
import jsonpickle


class ReviewExtended:
    def __init__(self, review_id:int, review_title:str, review_text:str, review_rating:int,
                 concert_date:datetime,user_name:str,first_name:str,last_name:str,venue_name:str,
                 city_name:str,country_name:str, tour_name:str, artist_name:str, tour_id:int,venue_id:int):
        self.review_id = review_id
        self.ReviewTitle = review_title
        self.ReviewText = review_text
        self.ReviewRating = review_rating
        self.ConcertDate = concert_date
        self.UserName = user_name
        self.FirstName = first_name
        self.LastName = last_name
        self.VenueName = venue_name
        self.CityName = city_name
        self.CountryName = country_name
        self.TourName = tour_name
        self.ArtistName = artist_name
        self.tour_id = tour_id
        self.venue_id = venue_id

    def to_json(self):
        return jsonpickle.encode(self,unpicklable=False)
