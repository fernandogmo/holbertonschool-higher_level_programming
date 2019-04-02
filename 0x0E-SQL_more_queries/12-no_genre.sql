-- List shows from database
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
RIGHT OUTER JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
WHERE genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
