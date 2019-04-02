-- List all shows not linked to Dexter
SELECT d.name
FROM tv_genres d
WHERE d.name NOT IN
(SELECT c.name
	FROM tv_shows a
	JOIN tv_show_genres b
	ON a.id = b.show_id
	JOIN tv_genres c
	ON b.genre_id = c.id
	WHERE a.title = 'Dexter')
ORDER BY d.name ASC;
