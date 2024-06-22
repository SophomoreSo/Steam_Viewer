CREATE DATABASE IF NOT EXISTS steamdb;
USE steamdb;

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

SET autocommit=0;
SET unique_checks=0;
SET foreign_key_checks=0;

LOAD DATA LOCAL INFILE 'price.csv' INTO TABLE price
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(app_id, timestamp, price);

LOAD DATA LOCAL INFILE 'game.csv' INTO TABLE game
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(app_id, game_name, rate_num, rate_positive);

COMMIT;
SET unique_checks=1;
SET foreign_key_checks=1;
