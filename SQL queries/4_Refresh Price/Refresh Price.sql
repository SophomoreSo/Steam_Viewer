-- Updated price --
INSERT INTO Price (app_id, timestamp, price) VALUES (400, CURRENT_TIMESTAMP, 0);
-- Game 'Portal' is now free!
-- Let's check the database
SELECT timestamp, price FROM price WHERE app_id = 400;