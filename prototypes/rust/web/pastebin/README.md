# Pastebin Copycat

- User gets the homepage/explaination content from the `/` route.
- User can post to `/` to push a new file.
  - Body contains exact content to be uploaded
  - Response returns an ID which is used to retrieve the content
- Use can retrieve this content with `/<id>`