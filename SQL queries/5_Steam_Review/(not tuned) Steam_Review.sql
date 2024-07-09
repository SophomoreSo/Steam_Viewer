SELECT user_id, voted_up, discussion_text, timestamp_created
FROM review_not_tuned
WHERE game_id = 413150
ORDER BY timestamp_created DESC
LIMIT 5;