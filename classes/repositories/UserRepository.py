from classes.models.Database import Database
from classes.models.User import User


class UserRepository(Database):
     # Get a user from the database with a given user_id
    def get_user_by_id(self, user_id:int):
        sql = 'SELECT * FROM public."Users" WHERE user_id = %s;' # Note: no quotes
        data = (user_id, )
        row = self.get_data(sql,data,True)
        print(row)
        user = User(row[0],row[1],row[2],row[3],row[4])
        return user.to_json()
    def get_user_object_by_id(self, user_id:int):
        sql = 'SELECT * FROM public."Users" WHERE user_id = %s;' # Note: no quotes
        data = (user_id, )
        row = self.get_data(sql,data,True)
        print(row)
        user = User(row[0],row[1],row[2],row[3],row[4])
        return user
    # Get a user from the database with a given UserName
    def get_user_by_username(self, user_name:str) -> User | None:
        sql = 'SELECT * FROM public."Users" WHERE "UserName" = %s;' # Note: no quotes
        data = (user_name, )
        row = self.get_data(sql,data,True)
        if row is None:
            return None
        print(row)
        return User(row[0],row[1],row[2],row[3],row[4])

    def get_user_by_username_json(self, user_name:str) -> str | None:
        sql = 'SELECT * FROM public."Users" WHERE "UserName" = %s;' # Note: no quotes
        data = (user_name, )
        row = self.get_data(sql,data,True)
        if row is None:
            return None
        print(row)
        user = User(row[0],row[1],row[2],row[3],row[4])
        return user.to_json()