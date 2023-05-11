import jsonpickle
from classes.models.Database import Database
from classes.models.Review import Review


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
    
    # Add a new review to the Review table
    def add_review(self, review:Review):
        sql = 'INSERT INTO public."Review" ("ReviewTitle","ReviewText","ReviewRating","user_id","concert_id") VALUES (%s,%s,%s,%s,%s) RETURNING review_id;'
        data = (review.ReviewTitle,review.ReviewText,review.ReviewRating,review.user_id,review.concert_id,)
        id_of_new_review = self.create_data(sql,data)
        review.review_id = id_of_new_review
        return review
    
    # Edit an existing review based on review_id
    def edit_review(self, review:Review):
        sql = 'UPDATE public."Review" SET "ReviewTitle" = %s,"ReviewText" = %s,"ReviewRating" = %s WHERE review_id = %s;'
        data = (review.ReviewTitle,review.ReviewText,review.ReviewRating,review.review_id,)
        return self.update_delete_data(sql,data)
    
    # Delete an existing review from the Review table
    def delete_review(self, review:Review):
        sql = 'DROP * FROM public."Review" WHERE review_id = %s;'
        data = (review.review_id,)
        return self.update_delete_data(sql,data)


    
