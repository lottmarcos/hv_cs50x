SELECT DISTINCT COUNT(movies.title)
FROM movies INNER JOIN ratings
WHERE ratings.rating = 10.0
AND ratings.movie_id = movies.id;