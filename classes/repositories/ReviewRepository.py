from flask import Response
import jsonpickle
from classes.models.Database import Database
from classes.models.Review import Review
from classes.models.ReviewExtended import ReviewExtended


class ReviewRepository(Database):
    # Get all review for a given user_id
    def get_reviews_by_user_id(self, user_id:int):
        sql = 'SELECT * FROM public."Review" WHERE user_id = %s;' # Note: no quotes
        data = (user_id, )
        rows = self.get_data(sql,data,False)
        res = []
        for x in range(len(rows)):
            review = Review(rows[x][0],rows[x][1],rows[x][2])
            res.append(review)
        return jsonpickle.encode(res, False)
    
    # Get all reviews for a given concert_id
    def get_reviews_by_concert_id(self,concert_id:int):
        sql = 'SELECT * FROM public."Review" WHERE concert_id = %s;' # Note: no quotes
        data = (concert_id, )
        rows = self.get_data(sql,data,False)
        res = []
        for x in range(len(rows)):
            review = Review(rows[x][0],rows[x][1],rows[x][2])
            res.append(review)
        return jsonpickle.encode(res, False)
    
    # Get all reviews a specifc artist
    def get_reviews_for_artist_id(self,artist_id:int):
        sql = """SELECT 
        public."Review"."review_id",
        public."Review"."ReviewTitle",
        public."Review"."ReviewText",
        public."Review"."ReviewRating",
        public."Concert"."ConcertDate",
        public."Users"."UserName",
        public."Users"."FirstName",
        public."Users"."LastName",
        public."Venue"."VenueName",
        public."City"."CityName",
        public."Country"."CountryName",
        public."Tour"."TourName",
        public."Artist"."ArtistName",
        public."Tour"."tour_id",
        poublic."Venue"."venue_id

        FROM public."Review" 
        NATURAL JOIN public."Concert" 
        NATURAL JOIN public."Venue"
        NATURAL JOIN public."Tour"
        NATURAL JOIN public."City"
        NATURAL JOIN public."Country"
        NATURAL JOIN public."Users"
        NATURAL JOIN public."Artist"
        WHERE artist_id = %s;"""
        data = (artist_id,)
        rows = self.get_data(sql,data,False)
        res = []
        for x in range(len(rows)):
            print(rows[x])
            review = ReviewExtended(rows[x][0],rows[x][1],rows[x][2],rows[x][3],
                                    rows[x][4],rows[x][5],rows[x][6],rows[x][7],
                                    rows[x][8],rows[x][9],rows[x][10],rows[x][11],rows[x][12],rows[x][13],rows[x][14])
            res.append(review)
        return jsonpickle.encode(res, False)
    
    # Get reviews for tour id
    def get_reviews_for_tour_id(self, tour_id:int):
        sql = """SELECT 
        public."Review"."review_id",
        public."Review"."ReviewTitle",
        public."Review"."ReviewText",
        public."Review"."ReviewRating",
        public."Concert"."ConcertDate",
        public."Users"."UserName",
        public."Users"."FirstName",
        public."Users"."LastName",
        public."Venue"."VenueName",
        public."City"."CityName",
        public."Country"."CountryName",
        public."Tour"."TourName",
        public."Artist"."ArtistName",
        public."Tour"."tour_id",
        public."Venue"."venue_id"

        FROM public."Review" 

        NATURAL JOIN public."Concert" 
        NATURAL JOIN public."Venue"
        NATURAL JOIN public."Tour"
        NATURAL JOIN public."City"
        NATURAL JOIN public."Country"
        NATURAL JOIN public."Users"
        NATURAL JOIN public."Artist"
        WHERE tour_id = %s;"""

        data = (tour_id,)
        rows = self.get_data(sql,data,False)
        res = []
        for x in range(len(rows)):
            print(rows[x])
            review = ReviewExtended(rows[x][0],rows[x][1],rows[x][2],rows[x][3],
                                    rows[x][4],rows[x][5],rows[x][6],rows[x][7],
                                    rows[x][8],rows[x][9],rows[x][10],rows[x][11],rows[x][12],rows[x][13],rows[x][14])
            res.append(review)
        return jsonpickle.encode(res, False)
    # Get reviews for venue id
    def get_reviews_for_venue_id(self, venue_id:int):
        sql = """SELECT 
        public."Review"."review_id",
        public."Review"."ReviewTitle",
        public."Review"."ReviewText",
        public."Review"."ReviewRating",
        public."Concert"."ConcertDate",
        public."Users"."UserName",
        public."Users"."FirstName",
        public."Users"."LastName",
        public."Venue"."VenueName",
        public."City"."CityName",
        public."Country"."CountryName",
        public."Tour"."TourName",
        public."Artist"."ArtistName",
        public."Tour"."tour_id",
        public."Venue"."venue_id"

        FROM public."Review" 

        NATURAL JOIN public."Concert" 
        NATURAL JOIN public."Venue"
        NATURAL JOIN public."Tour"
        NATURAL JOIN public."City"
        NATURAL JOIN public."Country"
        NATURAL JOIN public."Users"
        NATURAL JOIN public."Artist"
        WHERE venue_id = %s;"""

        data = (venue_id,)
        rows = self.get_data(sql,data,False)
        res = []
        for x in range(len(rows)):
            print(rows[x])
            review = ReviewExtended(rows[x][0],rows[x][1],rows[x][2],rows[x][3],
                                    rows[x][4],rows[x][5],rows[x][6],rows[x][7],
                                    rows[x][8],rows[x][9],rows[x][10],rows[x][11],rows[x][12],rows[x][13],rows[x][14])
            res.append(review)
        return jsonpickle.encode(res, False)

    # Add a new review to the Review table
    def add_review(self, review:Review):
        sql = 'INSERT INTO public."Review" ("ReviewTitle","ReviewText","ReviewRating","user_id","concert_id") VALUES (%s,%s,%s,%s,%s) RETURNING review_id;'
        data = (review.ReviewTitle,review.ReviewText,review.ReviewRating,review.user_id,review.concert_id,)
        id_of_new_review = self.create_data(sql,data)
        review.review_id = id_of_new_review
        return review.to_json()
    
    # Edit an existing review based on review_id
    def edit_review(self, review:Review):
        sql = 'UPDATE public."Review" SET "ReviewTitle" = %s,"ReviewText" = %s,"ReviewRating" = %s WHERE review_id = %s;'
        data = (review.ReviewTitle,review.ReviewText,review.ReviewRating,review.review_id,)
        self.update_delete_data(sql,data)
        return review.to_json()
    
    # Delete an existing review from the Review table
    def delete_review(self, review_id:int):
        sql = 'DELETE FROM public."Review" WHERE review_id = %s;'
        data = (review_id,)
        self.update_delete_data(sql,data)
        response = Response(status=200)
        return response


    
