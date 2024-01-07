#[macro_use]
extern crate rocket;

mod routes;
mod serde;
mod structs;

/// Launches the Rocket application
#[launch]
fn rocket() -> _ {
    rocket::build().mount("/api", routes::all())
}
