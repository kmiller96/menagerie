# PostgreSQL FTS

Did you know that postgres has FTS capabilities? And it comes with some very
basic NLP!

This prototype explores this functionality in postgres. Some articles for
further reading:

- https://admcpr.com/postgres-full-text-search-is-better-than-part1/
- https://www.postgresql.org/docs/current/textsearch.html
- https://www.crunchydata.com/blog/postgres-full-text-search-a-search-engine-in-a-database

## Connect

```bash
bash psql.sh
```

## Prototype

### Basic search using `like` and `ilike`

The most basic way of doing a FTS. Basically just looking for keywords within
a text column.

```sql
select title from movies where title like '%star%' limit 50;
select title from movies where title ilike '%star%' limit 50;
```

### Lexemes Search

`ts_vector` converts a string into a collection of lexemes i.e. words that are
normalised into a common form.

Here is an example:

```sql
select to_tsvector('I am altering the deal. Pray I don''t alter it any further!');
```

You can apply this function to a column. Here is an example:

```sql
select title, to_tsvector(title) from movies limit 20;
```

You can use `ts_query` to search over this vector of lexemes. You can also rank
the results using `ts_rank`.

```sql
select title, ts_rank(to_tsvector(title), to_tsquery('Star')) as rank
from movies
where to_tsvector(title) @@ to_tsquery('Star');
```

The `ts_query` function will only work for single words. If you have many words
in your search term you will need to use `plainto_tsquery` instead.

```sql
select title, ts_rank(to_tsvector(title), plainto_tsquery('star wars')) as rank
from movies
where to_tsvector(title) @@ plainto_tsquery('star wars')
order by rank desc
```

### Searching over Multiple columns

You can search over multiple columns using the concat (`||`) operator.

```sql
select
    to_tsvector(title)
    || ' '
    ||  to_tsvector(directors)
    || ' '
    || to_tsvector(stars)
    as vector
from
    movies
limit
    10
;
```
