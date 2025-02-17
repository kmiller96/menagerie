COPY test(id, name)
FROM '/mnt/data/test.csv'
DELIMITER ','
CSV HEADER;