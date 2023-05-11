import psycopg2
import os

# This is a helper class to handle connections with the PostgreSQL database hosted in elephantSQL, 
# as well as providing a set of common methods to perform CRUD operations on data
class Database:
    # Constructor for Database
    def __init__(self):
        self.connection_string = os.getenv('DB_CONNECTION_STRING')
        self.database_name = os.getenv('DB_DATABASE_NAME')
        self.user = os.getenv('DB_USER_NAME')
        self.password = os.getenv('DB_PASSWORD')

    # Private method to create a connection
    def __connect(self):
        return psycopg2.connect(
            host=self.connection_string,
            database=self.database_name,
            user=self.user,
            password=self.password)
    
    # Private method to close connection with db
    def __close(self, curr, conn):
        curr.close()
        conn.close()
    
    # Public method to get data by executing the supplied query and its associated data. 
    # Boolean toggle for whether to fetch 1 row or all matching rows (default to True)
    def get_data(self, query:str, data, single_row = True):
        # create a connection
        conn = self.__connect()
        
        # create a cursor
        cur = conn.cursor()
        
	    # execute a statement
        cur.execute(query, data)

        if single_row:
            # return single row of data as dict
            row = cur.fetchone()
            self.__close(cur,conn)
            return row

        else:
            # return array of rows
            rows = cur.fetchall()
            self.__close(cur,conn)
            return rows
        
    # Create a row in the database and return the id of the new row, or 0 if failed as 0 cannot be used as an id in database
    def create_data(self,sql:str,data):
        # create a connection
        conn = self.__connect()

        try:
            cur = conn.cursor()

            cur.execute(sql, data)

            id = cur.fetchone()[0]

            conn.commit()

            self.__close(cur,conn)

            return id
        
        except Exception as e:
            print(e.with_traceback())
            self.__close(cur,conn)
            return 0
        
    # Update or delete a row in any table using supplied sql statement and data
    # Returns a boolean to say if it was successful in its operation
    def update_delete_data(self, sql:str, data):
        # create a connection
        conn = self.__connect()
        
        try:
            cur = conn.cursor()

            cur.execute(sql, data)

            conn.commit()

            self.__close(cur,conn)

            return True
        except Exception as e:
            print(e.with_traceback())
            self.__close(cur,conn)
            return False

        






