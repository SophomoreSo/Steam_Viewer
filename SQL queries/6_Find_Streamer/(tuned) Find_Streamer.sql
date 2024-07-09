SELECT s.streamer_name, s.followers 
FROM streamer_app sa 
JOIN streamer s ON sa.streamer_id = s.streamer_id 
WHERE sa.app_id = 1245620;