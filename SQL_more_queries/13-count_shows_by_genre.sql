-- List all genres with the number of shows linked

SELECT GENRES.NAME AS genre, COUNT(TV_SHOW_GENRES.SHOW_ID) AS number_of_shows
FROM GENRES
JOIN TV_SHOW_GENRES ON GENRES.ID = TV_SHOW_GENRES.GENRE_ID
GROUP BY GENRES.ID
ORDER BY number_of_shows DESC;

