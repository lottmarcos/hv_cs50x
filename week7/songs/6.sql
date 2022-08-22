SELECT DISTINCT songs.name
FROM songs, artists
WHERE artists.name = "Post Malone"
   AND  songs.artist_id = artists.id;