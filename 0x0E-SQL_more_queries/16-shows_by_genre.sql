-- Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- Sorted in ascending order
SELECT s.title, g.name
FROM tv_shows s LEFT OUTER JOIN tv_show_genres sg
  ON s.id = sg.show_id
  LEFT OUTER JOIN tv_genres g
  ON sg.genre_id = g.id
ORDER BY s.title, g.name;
