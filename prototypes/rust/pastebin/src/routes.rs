use std::{fs, io::Write};

use md5;
use rocket::State;

use crate::config::Config;

/// Returns the vector of routes for the application.
///
/// This is used when mounting the routes to the rocket application.
pub fn routes() -> Vec<rocket::Route> {
    routes![index, upload, retrieve]
}

/// Returns the README for the application
#[get("/")]
fn index() -> String {
    String::from(include_str!("homepage.txt"))
}

/// Uploads a new file to the application
#[post("/", data = "<data>")]
fn upload(data: String, conf: &State<Config>) -> String {
    // Create an ID for the file
    let id = md5::compute(&data);
    let id = format!("{:x}", id);

    // Determine where we will write the file
    let mut path = conf.path.to_owned();
    path.push(&id);

    // Write the body to the file
    let mut file = fs::File::create(&path).expect("Failed to create file");
    write!(file, "{}", &data).expect("Failed to write to file");

    String::from(id)
}

/// Retrieve an already uploaded file
#[get("/<id>")]
fn retrieve(id: &str, conf: &State<Config>) -> Option<String> {
    // Build the filepath
    let mut path = conf.path.to_owned();
    path.push(&id);

    // Read the file contents
    fs::read_to_string(path).ok()
}
