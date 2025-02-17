-- +goose Up
-- +goose statementbegin
INSERT INTO A (id, name) VALUES (1, 'A1');
INSERT INTO A (id, name) VALUES (2, 'A2');
INSERT INTO A (id, name) VALUES (3, 'A3');

INSERT INTO B (id, name) VALUES (1, 'B1'), (2, 'B2'), (3, 'B3');
-- +goose statementend

------------------------------------------------------------
------------------------------------------------------------

-- +goose Down
-- +goose statementbegin
DELETE FROM A WHERE id IN (1, 2, 3);
DELETE FROM B WHERE id IN (1, 2, 3);
-- +goose statementend
