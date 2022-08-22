SELECT DISTINCT m.title
FROM people p1 INNER JOIN people p2 INNER JOIN movies m INNER JOIN stars s1 INNER JOIN stars s2
ON s1.movie_id = s2.movie_id AND s1.movie_id = m.id
AND s1.person_id = p1.id AND s2.person_id = p2.id
WHERE p1.name = "Johnny Depp" AND p2.name = "Helena Bonham Carter";