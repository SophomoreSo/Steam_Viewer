-- Show price history --
SELECT timestamp, price FROM Price WHERE app_id = 400 ORDER BY timestamp ASC;