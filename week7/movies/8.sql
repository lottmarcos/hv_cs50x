SELECT DISTINCT p.name
FROM people p INNER JOIN stars s INNER JOIN movies m
ON s.movie_id = m.id AND s.person_id = p.id
WHERE m.title LIKE "%Toy Story%";