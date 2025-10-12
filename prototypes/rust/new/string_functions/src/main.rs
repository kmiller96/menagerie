#[macro_use]
extern crate rocket;

#[get("/")]
fn health_check() -> &'static str {
    "{\"status\": \"OK\"}"
}

#[get("/test")]
fn test() -> &'static str {
    "{\"status\": \"OK\"}"
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![health_check, test])
}
