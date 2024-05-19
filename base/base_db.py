import mysql.connector
from mysql.connector import Error

class MySQLDatabase:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=3306
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: {e}")

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print(f"Record inserted: {self.cursor.rowcount}")
        except Error as e:
            print(f"Error: {e}")

    def delete(self, query, values):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print(f"Record deleted: {self.cursor.rowcount}")
        except Error as e:
            print(f"Error: {e}")

    def update(self, query, values):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print(f"Record updated: {self.cursor.rowcount}")
        except Error as e:
            print(f"Error: {e}")

    def select(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            return result
        except Error as e:
            print(f"Error: {e}")
            return None
