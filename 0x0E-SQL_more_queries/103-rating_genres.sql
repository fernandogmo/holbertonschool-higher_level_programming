-- List all genres by their ratings
SELECT a.name, sum(c.rate) AS rating
FROM tv_genres a
JOIN tv_show_genres b
ON a.id = b.genre_id
JOIN tv_show_ratings c
ON b.show_id = c.show_id
GROUP BY a.name
ORDER BY rating DESC;
