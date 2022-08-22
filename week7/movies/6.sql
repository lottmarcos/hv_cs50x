SELECT DISTINCT AVG(r.rating)
FROM movies m INNER JOIN ratings r
WHERE m.year = 2012
AND r.movie_id = m.id;