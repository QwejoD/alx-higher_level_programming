-- Lists all cities contained in the database hbtn_0d_usa.
-- Sorted in ascending order by cities.id
SELECT c.id AS id, c.name AS name, s.name AS name
FROM cities c INNER JOIN states s
  ON c.state_id = s.id
ORDER BY c.id
