# Python class representation of the User table in DB
from flask_login import UserMixin
from passlib.hash import pbkdf2_sha256
import jsonpickle

class User(UserMixin):
    def __init__(self, user_id:int,first_name:str, last_name:str,username:str,password:str):
        self.user_id = user_id
        self.FirstName = first_name
        self.LastName = last_name
        self.UserName = username
        self.Password = password

    def set_password(self, password):
       self.password_hash = pbkdf2_sha256.hash(password)

    def check_password(self, pw:str):
       print(pw)
       print(self.Password)
       is_match = pbkdf2_sha256.verify(pw.encode('utf-8'),self.Password.encode('utf-8'))
       print(is_match)
       return is_match

    def to_json(self):
        return jsonpickle.encode(self,unpicklable=False)
