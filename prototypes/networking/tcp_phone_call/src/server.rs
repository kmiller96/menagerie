use std::net::{TcpListener, TcpStream};

#[allow(unused_mut)] // TODO: Remove when implemented
fn handle_client(mut stream: TcpStream) {
    println!("New client: {}", stream.peer_addr().unwrap());
    // ...
    println!("Disconnected client: {}", stream.peer_addr().unwrap());
}

pub fn run_server(ip: String, port: u16) {
    // Initialise the listerner
    let listener = match TcpListener::bind((ip.as_str(), port)) {
        Ok(l) => l,
        Err(e) => {
            eprintln!("Failed to bind to {}:{} - {}", &ip, port, e);
            return;
        }
    };
    eprintln!(
        "Server listening on {}",
        listener.local_addr().expect("Failed to get local address")
    );

    // Handle incoming connections
    for stream in listener.incoming() {
        handle_client(stream.unwrap());
    }

    // Return
    return;
}
