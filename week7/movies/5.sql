SELECT DISTINCT movies.title, movies.year
FROM movies
WHERE movies.title LIKE "%Harry Potter%"
ORDER BY movies.year ASC;