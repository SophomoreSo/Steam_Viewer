CREATE DATABASE IF NOT EXISTS steamdb;
USE steamdb;
SHOW VARIABLES LIKE 'secure_file_priv';

CREATE TABLE IF NOT EXISTS game (
    app_id INT NOT NULL,
    game_name TEXT NOT NULL,
    rate_num INT DEFAULT 1 CHECK (rate_num > 0),
    rate_positive INT,
    PRIMARY KEY (app_id)
);

CREATE TABLE IF NOT EXISTS price (
    app_id INT NOT NULL,
    timestamp BIGINT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (app_id, timestamp)
);

CREATE TABLE IF NOT EXISTS Search (
    user_id BIGINT NOT NULL,
    -- https://www.w3schools.com/sql/sql_autoincrement.asp
    search_id INT AUTO_INCREMENT, -- easy way to generate id
    PRIMARY KEY (search_id)
);

CREATE TABLE IF NOT EXISTS Search_Param (
    search_id INT NOT NULL,
    keyword VARCHAR(255),
    min_price DECIMAL(10, 2) CHECK (min_price BETWEEN 0 AND 1000),
    max_price DECIMAL(10, 2) CHECK (max_price BETWEEN 0 AND 1000),
    min_review INT CHECK (min_review BETWEEN 0 AND 10000000),
    max_review INT CHECK (max_review BETWEEN 0 AND 10000000),
    min_rating INT CHECK (min_rating BETWEEN 0 AND 100),
    hl_only BOOL,
    CHECK (min_price <= max_price),
    CHECK (min_review <= max_review),
    PRIMARY KEY (search_id),
    FOREIGN KEY (search_id) REFERENCES Search(search_id) 
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Search_Name (
    search_id INT NOT NULL,
    search_name VARCHAR(255),
    PRIMARY KEY (search_id),
    FOREIGN KEY (search_id) REFERENCES Search(search_id)
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS review (
	discussion_id BIGINT NOT NULL, 
    game_id INT NOT NULL,
    PRIMARY KEY(discussion_id)
);

CREATE TABLE IF NOT EXISTS review_text (
	discussion_id BIGINT NOT NULL, 
    user_id BIGINT NOT NULL,
    voted_up BOOL NOT NULL,
    discussion_text TEXT,
    timestamp_created BIGINT NOT NULL,
    PRIMARY KEY(discussion_id),
    FOREIGN KEY(discussion_id) REFERENCES review(discussion_id)
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS streamer_app (
	streamer_id BIGINT NOT NULL, 
    app_id BIGINT NOT NULL,
    PRIMARY KEY(streamer_id)
);

CREATE TABLE IF NOT EXISTS streamer (
	streamer_id BIGINT NOT NULL, 
    streamer_name TEXT NOT NULL,
    followers BIGINT,
    PRIMARY KEY(streamer_id)
);

CREATE TABLE IF NOT EXISTS wishlist (
    user_id INT NOT NULL,
    app_id INT NOT NULL,
    wish_discount TINYINT NOT NULL CHECK (wish_discount BETWEEN 0 AND 100),
    PRIMARY KEY (user_id, app_id)
);

CREATE TABLE IF NOT EXISTS gameHL (
    app_id INT NOT NULL,
    price_hl DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (app_id)
);

CREATE TABLE IF NOT EXISTS game_description (
    game_id INT NOT NULL,
    short_description TEXT,
    PRIMARY KEY (game_id)
);

CREATE TABLE IF NOT EXISTS dlc (
    dlc_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    rate_num INT DEFAULT 1 CHECK (rate_num > 0),
    rate_positive INT DEFAULT 0,
    PRIMARY KEY (dlc_id)
);

CREATE TABLE IF NOT EXISTS soundtrack (
    soundtrack_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    rate_num INT DEFAULT 1 CHECK (rate_num > 0),
    rate_positive INT DEFAULT 0,
    PRIMARY KEY (soundtrack_id)
);

CREATE TABLE IF NOT EXISTS game_genre (
    game_id INT NOT NULL,
    genre varchar(30),
    PRIMARY KEY (game_id)
);

CREATE TABLE IF NOT EXISTS dlc_game (
    game_id INT NOT NULL,
    dlc_id INT NOT NULL,
    PRIMARY KEY (game_id, dlc_id),
    FOREIGN KEY (game_id) REFERENCES game(app_id),
    FOREIGN KEY (dlc_id) REFERENCES dlc(dlc_id)
);

SET autocommit=0;
SET unique_checks=0;
SET foreign_key_checks=0;

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/price.csv" INTO TABLE price
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(app_id, timestamp, price);

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/current_price.csv" INTO TABLE price
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(app_id, timestamp, price);

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/game_data.csv" INTO TABLE game
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(app_id, game_name, rate_num, rate_positive);

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/reviewID.csv" INTO TABLE review
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(discussion_id, game_id);

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/review.csv" INTO TABLE review_text
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(discussion_id, user_id, voted_up, discussion_text, timestamp_created);

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/streamers.csv" INTO TABLE streamer
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(streamer_id, streamer_name, followers);

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/streamer_app.csv" INTO TABLE streamer_app
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(streamer_id, app_id);

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/description.csv" INTO TABLE game_description
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(game_id,short_description);

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/dlc_data.csv" INTO TABLE dlc
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(dlc_id,name,rate_num,rate_positive);

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/soundtrack_data.csv" INTO TABLE soundtrack
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(soundtrack_id,name,rate_num,rate_positive);

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/genre.csv" INTO TABLE game_genre
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(game_id,genre);

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/dlc_id.csv" INTO TABLE dlc_game
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(game_id,dlc_id);

INSERT INTO gamehl (app_id, price_hl)
SELECT app_id, MIN(price)
FROM price
GROUP BY app_id;

COMMIT;
SET unique_checks=1;
SET foreign_key_checks=1;
