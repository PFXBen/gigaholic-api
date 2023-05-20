from flask import Blueprint, request
from classes.models.Review import Review
from classes.repositories.ReviewRepository import ReviewRepository

# Initialise repositories
review_repo = ReviewRepository()

# Example of a blueprint, this allows the declaration of flask routes in a different python file
review = Blueprint('review', __name__)

# Add new review
@review.post("/api/review/<int:user_id>")
def post_new_review(user_id):
    r = Review(0,request.form["ReviewTitle"],request.form["ReviewText"],request.form["ReviewRating"],user_id,request.form["concert_id"])
    return review_repo.add_review(r)

# Get reviews for a given artist
@review.get("/api/reviews/<int:artist_id>")
def get_reviews_for_artist_id(artist_id):
    return review_repo.get_reviews_for_artist_id(artist_id)

# Get reviews for a given tour
@review.get("/api/reviews/tour/<int:tour_id>")
def get_reviews_for_tour_id(tour_id):
    return review_repo.get_reviews_for_tour_id(tour_id)

# Get reviews for a given venue
@review.get("/api/reviews/venue/<int:venue_id>")
def get_reviews_for_venue_id(venue_id):
    return review_repo.get_reviews_for_venue_id(venue_id)

# Edit existing review
@review.patch("/api/review/<int:review_id>")
def patch_new_review(review_id):
    print(request.form)
    r = Review(review_id, request.form["ReviewTitle"],request.form["ReviewText"],request.form["ReviewRating"],request.form["user_id"],request.form["concert_id"])
    return review_repo.edit_review(r)

# Delete existing review
@review.delete("/api/review/<int:review_id>")
def delete_review(review_id):
    return review_repo.delete_review(review_id)
