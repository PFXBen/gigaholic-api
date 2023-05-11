# Python class representation of the Review table in DB
import jsonpickle


class Review:
    def __init__(self, review_id:int, review_title:str, review_text:str, review_rating:int, user_id:int, concert_id:int):
        self.review_id = review_id
        self.ReviewTitle = review_title
        self.ReviewText = review_text
        self.ReviewRating = review_rating
        self.user_id = user_id
        self.concert_id = concert_id

    def to_json(self):
        return jsonpickle.encode(self,unpicklable=False)
