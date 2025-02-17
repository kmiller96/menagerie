-- +goose Up
-- +goose statementbegin
create table A (
    id integer primary key,
    name text
);

create table B (
    id integer primary key,
    name text
);

create table C (
    id integer primary key,
    name text
);
-- +goose statementend

------------------------------------------------------------
------------------------------------------------------------

-- +goose Down
-- +goose statementbegin
drop table A;
drop table B;
drop table C;
-- +goose statementend
