use chrono::prelude::*;

#[macro_use]
extern crate rocket;

#[get("/")]
fn index() -> String {
    format!("{}", Utc::now().format("%Y-%m-%d %H:%M:%S"))
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![index])
}
