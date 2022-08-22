SELECT AVG(songs.energy)
FROM songs JOIN artists
WHERE artists.name = "Drake"
   AND songs.artist_id = artists.id;