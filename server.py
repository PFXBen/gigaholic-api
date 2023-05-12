from flask import Flask, request
from markupsafe import escape
from classes.models.Review import Review
from classes.repositories.ArtistRepository import ArtistRepository
from classes.repositories.UserRepository import UserRepository
from routes.ConcertBlueprint import concert
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Start flask server using the --app parameter passed in start commange
app = Flask(__name__)

# Include blueprints
app.register_blueprint(concert)

# Initialise repositories
user_repo = UserRepository()
artist_repo = ArtistRepository()

# routes go here
@app.get("/api/user/id/<int:user_id>")
def get_user_by_id(user_id):
    return user_repo.get_user_by_id(user_id)

@app.get("/api/user/username/<user_name>")
def get_user_by_username(user_name):
    return user_repo.get_user_by_username(escape(user_name))

@app.get("/api/artist/<int:artist_id>")
def get_artist_by_id(artist_id):
    return artist_repo.get_artist_by_id(artist_id)

@app.get("/api/artists/<int:genre_id>")
def get_artists_by_genre_id(genre_id):
    return artist_repo.get_artists_by_genre_id(genre_id)

@app.get("/api/artists")
def get_all_artists():
    return artist_repo.get_all_artists()

@app.post("/api/review")
def post_new_review():
    review = Review(0,request.body["ReviewTitle"],request.body["ReviewText"],request.body["ReviewRating"],request.body["user_id"],request.body["concert_id"])