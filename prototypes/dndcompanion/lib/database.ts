import postgres from "postgres";

const sql = postgres({
  // TODO: Make these environment variables
  host: "localhost",
  port: 5432,
  username: "admin",
  password: "admin",
  database: "default",
});

export default sql;
