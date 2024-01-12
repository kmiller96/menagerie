/// Returns all of the routes within the file.
pub fn all() -> Vec<rocket::Route> {
    routes![handlers::index, handlers::post, handlers::feed]
}

/// Contains all of the individual handlers
mod handlers {
    use postboard_structs::{Post, Submission};
    use rocket::serde::json::Json;

    use crate::db::Database;

    /// Simple health check to ensure that the server is working.
    #[get("/")]
    pub fn index() -> &'static str {
        "ok"
    }

    /// Submits a new post to the feed
    #[post("/post", data = "<data>")]
    pub fn post(data: Json<Submission>) -> Json<Post> {
        let data = data.into_inner();
        let post = Post::from_submission(data);

        Json(post)
    }

    /// Returns a collection of posts
    #[get("/feed")]
    pub fn feed() -> Json<Vec<Post>> {
        let mut db = Database::new().unwrap();
        let data = db.get_posts(10).unwrap();

        Json(data)
    }
}
