import mysql.connector

class SqlConnector:
    def __init__(self, passwd):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd=passwd,
            database="steamdb"
        )
        self.cursor = self.mydb.cursor()

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
class SqlOp:
    def __init__(self, passwd):
        self.sql = SqlConnector(passwd)
    
    def advancedSearch(self, name, min_price, max_price, min_rating, max_rating, user_rating):
        sql = f'''
            CREATE OR REPLACE VIEW SearchResult AS
            SELECT g.app_id, g.game_name, p.price, g.rate_num, g.rate_positive
            FROM Game g
            JOIN Price p ON g.app_id = p.app_id
            JOIN (
                    SELECT app_id, MAX(timestamp) AS latest_timestamp
                    FROM Price
                    GROUP BY app_id
                ) lp ON 
                    p.app_id = lp.app_id 
                    AND p.timestamp = lp.latest_timestamp
            WHERE 
                g.game_name LIKE '%{name}%'
                AND g.rate_num BETWEEN {min_rating} AND {max_rating}
                AND (g.rate_positive * 100.0 / g.rate_num) >= {user_rating}
                AND p.price BETWEEN {min_price} AND {max_price};
            '''
        self.sql.query(sql)

    def getCountFromSearchResult(self):
        sql = "SELECT COUNT(*) FROM SearchResult;"
        return self.sql.query(sql)
        
    def getSearchResult(self, limit, page, order_by, is_ascend):
        sql = f'''SELECT * FROM SearchResult 
                ORDER BY {order_by} {'ASC' if is_ascend else 'DESC'} 
                LIMIT {limit} 
                OFFSET {limit * (page - 1)};'''
        return self.sql.query(sql)
    
    def getGameById(self, id):
        sql = f"SELECT app_id, game_name, rate_num, rate_positive FROM game WHERE app_id = {id}"
        return self.sql.query(sql)
    
    def getPriceById(self, app_id):
        sql = f"SELECT price FROM price WHERE app_id = {app_id} ORDER BY timestamp DESC LIMIT 1;"
        return self.sql.query(sql)
    
    def getPriceHistoryById(self, app_id):
        sql = f"SELECT timestamp, price FROM price WHERE app_id = {app_id} ORDER BY timestamp ASC;"
        return self.sql.query(sql)
    
    def getReviewByAppId(self, app_id):
        sql = f'''SELECT rt.user_id, rt.voted_up, rt.discussion_text, rt.timestamp_created
                FROM review_text rt
                JOIN review r ON rt.discussion_id = r.discussion_id
                WHERE r.game_id = {app_id}
                ORDER BY rt.timestamp_created DESC
                LIMIT 5;'''
        return self.sql.query(sql)
    
    def insertPrice(self, app_id, price):
        sql = f"INSERT INTO price (app_id, timestamp, price) VALUES ({app_id}, {price})"
        self.sql.query(sql)