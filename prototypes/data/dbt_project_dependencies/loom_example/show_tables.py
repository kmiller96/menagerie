import duckdb

with duckdb.connect(database="warehouse.duckdb") as con:
    print(con.sql("SHOW TABLES;"))
