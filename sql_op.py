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
    
    def commit(self):
        self.mydb.commit()
    
class SqlOp:
    def __init__(self, passwd):
        self.sql = SqlConnector(passwd)
    
    def advancedSearch(self, name, min_price, max_price, min_rating, max_rating, user_rating):      
        sql = f"DROP TEMPORARY TABLE IF EXISTS SearchResult;"
        self.sql.query(sql)
        sql = f'''
            CREATE TEMPORARY TABLE SearchResult AS
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

    def advancedSearchWithHL(self, name, min_price, max_price, min_rating, max_rating, user_rating):      
        sql = f"DROP TEMPORARY TABLE IF EXISTS SearchResult;"
        self.sql.query(sql)
        sql = f'''CREATE TEMPORARY TABLE SearchResult AS
                SELECT 
                    g.app_id, 
                    g.game_name, 
                    p.price, 
                    g.rate_num, 
                    g.rate_positive
                FROM Game g
                JOIN Price p ON g.app_id = p.app_id
                JOIN 
                    (
                        SELECT 
                            app_id, 
                            MAX(timestamp) AS latest_timestamp
                        FROM 
                            Price
                        GROUP BY 
                            app_id
                    ) lp ON p.app_id = lp.app_id 
                        AND p.timestamp = lp.latest_timestamp
                JOIN 
                    gamehl gh ON g.app_id = gh.app_id
                WHERE 
                    g.game_name LIKE '%{name}%'
                    AND g.rate_num BETWEEN {min_rating} AND {max_rating}
                    AND (g.rate_positive * 100.0 / g.rate_num) >= {user_rating}
                    AND p.price BETWEEN {min_price} AND {max_price}
                    AND gh.price_hl > p.price;
            '''
        self.sql.query(sql)

    def searchDLCs(self, app_id):
        sql = f"DROP TEMPORARY TABLE IF EXISTS SearchResult;"
        self.sql.query(sql)
        sql = f'''
                CREATE TEMPORARY TABLE SearchResult AS
                SELECT
                    dlc.dlc_id AS app_id,
                    dlc.name AS game_name,
                    p.price AS price,
                    dlc.rate_num AS rate_num,
                    dlc.rate_positive AS rate_positive
                FROM dlc_game
                JOIN dlc ON dlc_game.dlc_id = dlc.dlc_id
                JOIN
                    (SELECT app_id, price
                    FROM price p1
                    WHERE timestamp = (SELECT MAX(timestamp)
                                        FROM price p2
                                        WHERE p1.app_id = p2.app_id)) p
                ON dlc.dlc_id = p.app_id
                WHERE dlc_game.game_id = {app_id}
                UNION ALL
                SELECT
                    soundtrack.soundtrack_id AS app_id,
                    soundtrack.name AS game_name,
                    soundtrack.rate_num AS rate_num,
                    soundtrack.rate_positive AS rate_positive,
                    p.price AS price
                FROM dlc_game
                JOIN soundtrack ON dlc_game.dlc_id = soundtrack.soundtrack_id
                JOIN
                    (SELECT app_id, price
                    FROM price p1
                    WHERE timestamp = (SELECT MAX(timestamp)
                                        FROM price p2
                                        WHERE p1.app_id = p2.app_id)) p
                ON soundtrack.soundtrack_id = p.app_id
                WHERE dlc_game.game_id = {app_id};
            '''
        self.sql.query(sql)
    
    def getHistoricalLow(self, app_id):
        sql = f'''
            SELECT price_hl FROM gamehl WHERE app_id = {app_id};
            '''
        return self.sql.query(sql)
    
    def getGamesOnSale(self):
        # gets wishlisted games on sales
        pass

    def getCountFromSearchResult(self):
        sql = "SELECT COUNT(app_id) FROM SearchResult;"
        return self.sql.query(sql)
        
    def getSearchResult(self, limit, page, order_by, is_ascend):
        sql = f'''SELECT 
                        sr.app_id, 
                        sr.game_name, 
                        sr.price, 
                        sr.rate_num, 
                        sr.rate_positive, 
                        gh.price_hl 
                    FROM SearchResult sr
                    LEFT JOIN gamehl gh ON sr.app_id = gh.app_id
                    ORDER BY {order_by} {('ASC' if is_ascend else 'DESC')}
                    LIMIT {limit} 
                    OFFSET {limit * (page - 1)};'''
        return self.sql.query(sql)
    
    def getGameById(self, id):
        sql = f'''SELECT app_id, game_name, rate_num, rate_positive FROM game WHERE app_id = {id}
                UNION ALL
                SELECT dlc_id, name, rate_num, rate_positive FROM dlc WHERE dlc_id = {id}
                UNION ALL
                SELECT soundtrack_id, name, rate_num, rate_positive FROM soundtrack WHERE soundtrack_id = {id};
        '''
        return self.sql.query(sql)
    
    def getPriceById(self, app_id):
        sql = f"SELECT price FROM price WHERE app_id = {app_id} ORDER BY timestamp DESC LIMIT 1;"
        return self.sql.query(sql)
    
    def getPriceHistoryById(self, app_id):
        sql = f"SELECT timestamp, price FROM price WHERE app_id = {app_id} ORDER BY timestamp ASC;"
        return self.sql.query(sql)
    
    def getDescriptionById(self, app_id):
        sql = f"SELECT short_description FROM game_description WHERE game_id = {app_id}"
        return self.sql.query(sql)
    
    def getGameGenresById(self, app_id):
        sql = f'''SELECT genre FROM game_genre WHERE game_id = {app_id};'''
        return self.sql.query(sql)
    
    def getReviewByAppId(self, app_id):
        sql = f'''SELECT rt.user_id, rt.voted_up, rt.discussion_text, rt.timestamp_created
                FROM review_text rt
                JOIN review r ON rt.discussion_id = r.discussion_id
                WHERE r.game_id = {app_id}
                ORDER BY rt.timestamp_created DESC
                LIMIT 5;'''
        return self.sql.query(sql)
    
    def getStreamerList(self, app_id):
        sql = f'''SELECT s.streamer_id, s.streamer_name, s.followers 
                    FROM streamer_app sa 
                    JOIN streamer s ON sa.streamer_id = s.streamer_id 
                    WHERE sa.app_id = {app_id}
                    ORDER BY s.followers DESC;'''
        return self.sql.query(sql)
    
    def insertPrice(self, app_id, price):
        sql = f"INSERT INTO price (app_id, timestamp, price) VALUES ({app_id}, {price})"
        self.sql.query(sql)

    def isDuplicateWishlist(self, user_id, app_id):
        sql = f"SELECT COUNT(app_id) FROM wishlist WHERE user_id = {user_id} AND app_id = {app_id}"
        count = self.sql.query(sql)[0][0]
        if count == 0:
            return False
        else:
            return True

    def addWishlist(self, user_id, app_id, discount):
        sql = f"INSERT INTO wishlist (user_id, app_id, wish_discount) VALUES ({user_id}, {app_id}, {discount})"
        self.sql.query(sql)
        self.sql.commit()

    def getWishlist(self, user_id):
        sql = f'''SELECT g.app_id, g.game_name, w.wish_discount
                FROM wishlist w
                JOIN game g ON w.app_id = g.app_id
                WHERE w.user_id = {user_id};'''
        return self.sql.query(sql)
    
    def deleteWishlist(self, user_id, app_id):
        sql = f"DELETE FROM wishlist WHERE user_id = {user_id} AND app_id = {app_id}"
        self.sql.query(sql)

    def updateWishlist(self, user_id, app_id, discount):
        sql = f"UPDATE wishlist SET wish_discount = {discount} WHERE user_id = {user_id} AND app_id = {app_id}"
        self.sql.query(sql)

    def saveParameter(self, user_id, saved_name, keyword, min_price, max_price, min_review, max_review, min_rating, hl_only):
        sql = f"INSERT INTO Search (user_id) VALUES ({user_id})"
        self.sql.query(sql)
        # Retrieves the last inserted search_id
        sql = f"SELECT LAST_INSERT_ID()"
        search_id = self.sql.query(sql)[0][0]
        sql = f"INSERT INTO Search_Param (search_id, keyword, min_price, max_price, min_review, max_review, min_rating, hl_only) VALUES ({search_id}, '{keyword}', {min_price}, {max_price}, {min_review}, {max_review}, {min_rating}, {hl_only})"
        self.sql.query(sql)
        sql = f"INSERT INTO Search_Name (search_id, search_name) VALUES ({search_id}, '{saved_name}')"
        self.sql.query(sql)
        self.sql.commit()

    def deleteParameter(self, user_id, search_id):
        sql = f"DELETE FROM Search WHERE user_id = {user_id} AND search_id = {search_id}"
        self.sql.query(sql)
        self.sql.commit()

    def getSavedParameter(self, user_id):
        sql = f'''SELECT search_id FROM Search WHERE user_id = {user_id};'''
        search_ids = self.sql.query(sql)
        search_ids = [search_id[0] for search_id in search_ids]
        search_ids = ', '.join(map(str, search_ids))
        if search_ids == '':
            return []
        sql = f'''SELECT sn.search_id, sn.search_name, sp.keyword, sp.min_price, sp.max_price, sp.min_review, sp.max_review, sp.min_rating, sp.hl_only
                FROM Search_Name sn
                JOIN Search_Param sp ON sn.search_id = sp.search_id
                WHERE sn.search_id IN ({search_ids});'''
        return self.sql.query(sql)