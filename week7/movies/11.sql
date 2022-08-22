SELECT m.title
FROM people p INNER JOIN movies m INNER JOIN ratings r INNER JOIN stars s
ON r.movie_id = m.id AND s.movie_id = m.id AND s.person_id = p.id
WHERE p.name = "Chadwick Boseman"
ORDER BY r.rating DESC
LIMIT 5;