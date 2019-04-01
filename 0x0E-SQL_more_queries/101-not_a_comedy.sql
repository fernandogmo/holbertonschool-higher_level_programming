-- List all shows not from the comedy genre
SELECT d.title
FROM tv_shows d
WHERE d.title NOT IN
(SELECT a.title
	FROM tv_shows a
	JOIN tv_show_genres b
	ON a.id = b.show_id
	JOIN tv_genres c
	ON b.genre_id = c.id
	WHERE c.name = 'Comedy')
ORDER BY d.title ASC;
