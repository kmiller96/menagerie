use chrono::prelude::*;

#[macro_use]
extern crate rocket;

#[get("/?<format>")]
fn index(format: Option<&str>) -> String {
    format!(
        "{}",
        Utc::now().format(format.unwrap_or("%Y-%m-%d %H:%M:%S"))
    )
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![index])
}
