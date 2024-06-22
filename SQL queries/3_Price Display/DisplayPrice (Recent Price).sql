-- Show most recent price --
SELECT price FROM price WHERE app_id = 400 ORDER BY timestamp DESC LIMIT 1;