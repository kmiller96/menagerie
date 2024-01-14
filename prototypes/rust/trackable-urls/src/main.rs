#[macro_use]
extern crate rocket;

use std::env;

use rocket::fs::NamedFile;
use rocket::State;

mod data;
use data::DocumentMap;

/// Fetches a document for the user given an ID
#[get("/<id>")]
async fn fetch(id: &str, db: &State<DocumentMap>) -> Option<NamedFile> {
    match db.get(&id) {
        Some(doc) => NamedFile::open(doc).await.ok(),
        None => None,
    }
}

#[launch]
fn rocket() -> _ {
    // Initialise the document map
    let mut root = env::current_dir().expect("Expected to be able to read current directory");
    root.push("documents");

    let mut map = DocumentMap::new(root);
    map.load("mapping.json".to_string());

    // Build the rocket
    rocket::build().manage(map).mount("/", routes![fetch])
}
