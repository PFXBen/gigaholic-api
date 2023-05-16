# Python class representation of the User table in DB
from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256
from werkzeug.security import check_password_hash, generate_password_hash
import jsonpickle

class User(UserMixin):
    def __init__(self, user_id:int,first_name:str, last_name:str,username:str,password:str):
        self.user_id = user_id
        self.FirstName = first_name
        self.LastName = last_name
        self.UserName = username
        self.Password = password

    def get_id(self):
        return self.user_id

    def set_password(self, password):
       self.password_hash = generate_password_hash(password)

    def check_password(self, pw:str):
       pw_hashed = check_password_hash(self.Password, pw)
       print(pw_hashed, self.Password)
       return pw_hashed

    def to_json(self):
        return jsonpickle.encode(self,unpicklable=False)
