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
#[get("/reverse")]
fn reverse() {
    // stub
}

/// Converts the input string to uppercase
#[get("/upper")]
fn upper() {
    // stub
}

/// Converts the input string to lowercase
#[get("/lower")]
fn lower() {
    // stub
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
