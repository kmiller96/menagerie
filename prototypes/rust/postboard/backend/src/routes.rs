use rocket::serde::json::Json;

use crate::structs::Post;

/// Returns all of the routes within the file.
pub fn all() -> Vec<rocket::Route> {
    routes![index, feed]
}

/// Simple health check to ensure that the server is working.
#[get("/")]
fn index() -> &'static str {
    "ok"
}

/// Returns a collection of posts
///
/// TODO: Order the posts in creation date order.
#[get("/feed")]
fn feed() -> Json<Vec<Post>> {
    Json(vec![
        Post::new(None, String::from("Post #1")),
        Post::new(None, String::from("Post #2")),
    ])
}
