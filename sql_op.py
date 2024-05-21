import mysql.connector

class SqlConnector:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="password edited for security",
            database="game_data"
        )
        self.cursor = self.mydb.cursor()
    
    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
class SqlOp:
    def __init__(self):
        self.sql = SqlConnector()
    
    def getGameByName(self, name):
        sql = f"SELECT * FROM game_encoded WHERE game_name = '{name}'"
        print("query:", sql)
        result = self.sql.query(sql)
        print(result)
        return result

if __name__ == "__main__":
    sql = SqlOp()
    print(sql.getGameByName('Team'))

