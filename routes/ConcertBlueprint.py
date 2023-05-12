from flask import Blueprint
from classes.repositories.ConcertRepository import ConcertRepository

# Initialise repositories
concert_repo = ConcertRepository()

# Example of a blueprint, this allows the declaration of flask routes in a different python file
concert = Blueprint('concert', __name__)
@concert.get('/api/concert/id/<int:concert_id>')
def get_concert_by_concert_id(concert_id):
    return concert_repo.get_concert_by_id(concert_id)