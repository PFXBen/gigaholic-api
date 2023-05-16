from flask import Blueprint
from markupsafe import escape
from classes.repositories.UserRepository import UserRepository

user_repo = UserRepository()

# Example of a blueprint, this allows the declaration of flask routes in a different python file
user = Blueprint('user', __name__)
@user.get("/api/user/id/<int:user_id>")
def get_user_by_id(user_id):
    return user_repo.get_user_by_id(user_id)

@user.get("/api/user/username/<user_name>")
def get_user_by_username(user_name):
    return user_repo.get_user_by_username_json(escape(user_name))