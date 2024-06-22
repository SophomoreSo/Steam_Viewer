-- Advanced Search Feature --
CREATE OR REPLACE VIEW SearchResult AS
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
	g.game_name LIKE '%Portal%'
	AND g.rate_num BETWEEN 100 AND 500000
	AND (g.rate_positive * 100.0 / g.rate_num) >= 80.0
	AND p.price BETWEEN 0 AND 20
LIMIT 10
OFFSET 0;

-- Sort By Feature --
SELECT * FROM SearchResult ORDER BY rate_num DESC;