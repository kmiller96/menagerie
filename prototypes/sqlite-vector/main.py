import importlib.resources
import sqlite3


def main():
    ## Open database connection ##
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row

    ## Load the sqlite-vector extension ##
    conn.enable_load_extension(True)
    conn.load_extension(
        str(importlib.resources.files("sqlite_vector.binaries") / "vector")
    )
    conn.enable_load_extension(False)

    ## Setup the database and insert some data ##
    conn.executescript(
        """
        CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT, embedding BLOB);

        SELECT vector_init('items', 'embedding', 'type=FLOAT32,dimension=3');

        INSERT INTO items (name, embedding) VALUES ('item1', vector_as_f32('[1.0, 2.0, 3.0]'));
        INSERT INTO items (name, embedding) VALUES ('item2', vector_as_f32('[4.0, 5.0, 6.0]'));
        INSERT INTO items (name, embedding) VALUES ('item3', vector_as_f32('[7.0, 8.0, 9.0]'));
        INSERT INTO items (name, embedding) VALUES ('item4', vector_as_f32('[2.0, 3.0, 4.0]'));
        """
    )

    ## Perform a vector search using the full scan method ##
    print(
        [
            dict(x)
            for x in conn.execute(
                """
                SELECT rowid, distance
                FROM vector_full_scan('items', 'embedding', vector_as_f32('[3.0, 3.0, 3.0]'))
                ORDER BY distance
                LIMIT 10;
                """
            ).fetchall()
        ]
    )

    ## Close connection ##
    conn.close()


if __name__ == "__main__":
    main()
