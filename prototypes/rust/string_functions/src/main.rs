#[macro_use]
extern crate rocket;

// ------------ //
// -- Routes -- //
// ------------ //

/// Simple healthcheck to verify the server is running
#[get("/")]
fn health_check() -> &'static str {
    "{\"status\": \"OK\"}"
}

/// Reverses the input string
#[get("/reverse?<input>")]
fn reverse(input: &str) -> String {
    input.chars().rev().collect()
}

/// Converts the input string to uppercase
#[get("/upper?<input>")]
fn upper(input: String) -> String {
    input.to_uppercase()
}

/// Converts the input string to lowercase
#[get("/lower?<input>")]
fn lower(input: String) -> String {
    input.to_lowercase()
}

#[get("/test")]
fn stub() -> &'static str {
    "stubby :("
}

// ------------ //
// -- Launch -- //
// ------------ //

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![health_check, reverse, upper, lower, stub])
}
