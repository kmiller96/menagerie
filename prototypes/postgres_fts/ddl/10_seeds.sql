COPY movies
FROM '/mnt/data/movies.csv'
DELIMITER ','
CSV HEADER;