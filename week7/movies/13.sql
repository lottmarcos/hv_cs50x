SELECT p.name
FROM stars s JOIN people p
ON s.person_id = p.id
WHERE movie_id IN
(  SELECT movie_id
   FROM people JOIN stars
   ON stars.person_id = people.id
   WHERE people.birth = 1958 AND people.name = "Kevin Bacon")
AND p.name != "Kevin Bacon";
