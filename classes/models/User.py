# Python class representation of the User table in DB
import jsonpickle

class User:
    def __init__(self, user_id:int,first_name:str, last_name:str,username:str,password:str):
        self.user_id = user_id
        self.FirstName = first_name
        self.LastName = last_name
        self.UserName = username
        self.Password = password

    def to_json(self):
        return jsonpickle.encode(self,unpicklable=False)