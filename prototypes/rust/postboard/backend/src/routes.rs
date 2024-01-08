/// Returns all of the routes within the file.
pub fn all() -> Vec<rocket::Route> {
    routes![handlers::index, handlers::post, handlers::feed]
}

/// Contains all of the individual handlers
mod handlers {
    use postboard_types::{Post, Submission};
    use rocket::serde::json::Json;

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
}
