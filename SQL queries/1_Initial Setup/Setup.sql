CREATE DATABASE IF NOT EXISTS steamdb;
USE steamdb;
SHOW VARIABLES LIKE 'secure_file_priv';
CREATE TABLE IF NOT EXISTS price (
    app_id INT NOT NULL,
    timestamp BIGINT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (app_id, timestamp)
);

CREATE TABLE IF NOT EXISTS game (
    app_id INT NOT NULL,
    game_name TEXT NOT NULL,
    rate_num INT,
    rate_positive INT,
    PRIMARY KEY (app_id)
);

CREATE TABLE IF NOT EXISTS wishlist (
    app_id INT NOT NULL,
    wish_price DECIMAL(10, 2) NOT NULL,
    wish_hl BOOL NOT NULL,
    alert BOOL NOT NULL,
    PRIMARY KEY (app_id)
);

CREATE TABLE IF NOT EXISTS parameter (
    app_id INT NOT NULL,
    wish_price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (app_id)
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
    PRIMARY KEY(discussion_id)
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

-- Tables not tuned for performance comparison --
CREATE TABLE IF NOT EXISTS streamer_not_tuned (
	app_id BIGINT NOT NULL,
    streamer_id BIGINT NOT NULL, 
    streamer_name TEXT NOT NULL,
    followers BIGINT,
    PRIMARY KEY(streamer_id)
);

CREATE TABLE IF NOT EXISTS review_not_tuned (
	game_id BIGINT NOT NULL,
    discussion_id BIGINT NOT NULL, 
    user_id BIGINT NOT NULL,
    voted_up BOOL NOT NULL,
    discussion_text TEXT,
    timestamp_created BIGINT NOT NULL,
    PRIMARY KEY(discussion_id)
);

SET autocommit=0;
SET unique_checks=0;
SET foreign_key_checks=0;

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/price.csv" INTO TABLE price
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(app_id, timestamp, price);

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/game.csv" INTO TABLE game
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

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/review_not_tuned.csv" INTO TABLE review_not_tuned
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(game_id, discussion_id, user_id, voted_up, discussion_text, timestamp_created);

LOAD DATA LOCAL INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/streamers_not_tuned.csv" INTO TABLE streamer_not_tuned
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(app_id, streamer_id, streamer_name, followers);

COMMIT;
SET unique_checks=1;
SET foreign_key_checks=1;
