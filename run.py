import os
from flask import Flask, render_template
from flask_login import LoginManager, current_user, login_required
from classes.repositories.UserRepository import UserRepository
from routes.ConcertBlueprint import concert
from routes.AuthBlueprint import auth
from routes.UserBlueprint import user
from routes.ArtistBlueprint import artist
from routes.ReviewBlueprint import review
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Start flask server using the --app parameter passed in start commange
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

#Init Repos
user_repo = UserRepository()

# Include blueprints
app.register_blueprint(concert)
app.register_blueprint(auth)
app.register_blueprint(user)
app.register_blueprint(artist)
app.register_blueprint(review)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return user_repo.get_user_object_by_id(user_id)

#Page Routes
@app.route("/")
@login_required
def index():
    print(current_user)
    return render_template("index.html", user=current_user)

@app.route("/reviews_by_artist")
@login_required
def by_artist():
    return render_template("by-artist.html")

@app.route("/reviews_by_tour")
@login_required
def by_tour():
    return render_template("by-tour.html")

@app.route("/reviews_by_venue")
@login_required
def by_venue():
    return render_template("by-venue.html")
