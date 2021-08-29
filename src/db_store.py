import sqlite3

class SqliteDataStore:
    def __init__(self):
        self.con = sqlite3.connect('example.db')
    def createTableIfNotExists(self):
        self.con.execute(
            '''
            CREATE TABLE analytics (
                id int PRIMARY KEY AUTO_INCREMENT,
                url varchar(255) NOT NULL,
                status_code int NOT NULL,
                elapsed_time FLOAT(6) NOT NULL,
                created timestamp NOT NULL)
            '''.replace("\n"," ")
        )
    def storeData(self,data:tuple):
        sqlite_insert_with_param = """INSERT INTO 'analytics'
                              ('url', 'status_code', 'elapsed_time', 'created') 
                              VALUES (?, ?, ?,?);"""
        self.con.execute(sqlite_insert_with_param, data)