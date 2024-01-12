use rocket::serde::json::Json;

use crate::db::Database;
use crate::structs::{Post, Submission};

////////////////
// Public API //
////////////////

/// Returns all of the routes within the file.
pub fn all() -> Vec<rocket::Route> {
    routes![index, post, feed]
}

////////////
// Routes //
////////////

/// Simple health check to ensure that the server is working.
#[get("/")]
fn index() -> &'static str {
    "ok"
}

/// Submits a new post to the feed
#[post("/post", data = "<data>")]
fn post(data: Json<Submission>) -> Json<Post> {
    let mut post = data.into_inner().to_post();

    let mut db = Database::new().unwrap();
    let row_id = db.create_post(&post).unwrap();

    post.id = Some(row_id);

    Json(post)
}

/// Returns a collection of posts
#[get("/feed")]
fn feed() -> Json<Vec<Post>> {
    let mut db = Database::new().unwrap();
    let data = db.get_posts(10).unwrap();

    Json(data)
}
