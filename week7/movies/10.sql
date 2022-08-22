SELECT DISTINCT p.name
FROM people p INNER JOIN movies m INNER JOIN ratings r INNER JOIN directors d
ON p.id = d.person_id AND m.id = d.movie_id AND r.movie_id = m.id
WHERE r.rating >= 9.0;