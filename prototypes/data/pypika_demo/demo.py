from pypika import Query, Table
from pypika.queries import QueryBuilder

users = Table("users")

query: QueryBuilder = Query.from_(users)

query = query.limit(10)
query = query.select("id", "name")
query = query.where(users.name == "Tom")

print(query.get_sql())
