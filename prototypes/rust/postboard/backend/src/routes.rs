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
#[get("/feed")]
fn feed() -> Json<Vec<Post>> {
    ///////////////////////////////////////////
    // NOTE: Temporary data used for testing //
    ///////////////////////////////////////////

    let post1 = Post::new(None, String::from("Post #1"));
    let post2 = Post::new(None, String::from("Post #2"));

    let mut data = vec![post2, post1]; // Simulates results being out of order

    ///////////////////////////////////////////

    data.sort_by_key(|el| el.created); // NOTE: Should sorting be delegated to the DB?
    Json(data)
}
