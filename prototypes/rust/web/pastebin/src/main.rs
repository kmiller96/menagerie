#[macro_use]
extern crate rocket;

mod config;
mod routes;

use routes::routes;

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(config::Config::new())
        .mount("/", routes())
}
