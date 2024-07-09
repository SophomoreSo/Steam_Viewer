SELECT rt.user_id, rt.voted_up, rt.discussion_text, rt.timestamp_created
FROM review_text rt
JOIN review r ON rt.discussion_id = r.discussion_id
WHERE r.game_id = 413150
ORDER BY rt.timestamp_created DESC
LIMIT 5;