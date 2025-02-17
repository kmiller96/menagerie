-- Alters the A table by adding a new column, age.

-- +goose Up
-- +goose statementbegin
ALTER TABLE A ADD COLUMN age integer;
UPDATE A SET age = 20 WHERE id = 1;
-- +goose statementend

-- +goose Down
ALTER TABLE A DROP COLUMN age;