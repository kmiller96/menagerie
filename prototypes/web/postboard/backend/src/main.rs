#[macro_use]
extern crate rocket;

mod structs;
mod routes;
mod db;

/// Launches the Rocket application
#[launch]
fn rocket() -> _ {
    rocket::build().mount("/api", routes::all())
}
