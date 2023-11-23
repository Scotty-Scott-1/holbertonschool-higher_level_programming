-- list all the shows and all genres linked to a show. If no genre display NULL
SELECT tv_shows.title, COALESCE(tv_genres.name, 'NULL') AS name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, COALESCE(tv_genres.name, 'NULL') ASC;
