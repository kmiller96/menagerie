#[allow(unused_imports)]
use std::{
    io::{Read, Write},
    net::{TcpListener, TcpStream},
};

const BUFFER_SIZE: usize = 512;

// ---------------------- //
// -- Public Functions -- //
// ---------------------- //

pub fn run_server(ip: String, port: u16) -> std::io::Result<()> {
    let listener = initialise(ip, port)?;

    for connection in listener.incoming() {
        match connection {
            Ok(stream) => handle_connection(stream)?,
            Err(e) => eprintln!("Skipping failed connection. Error: {}", e),
        }
    }

    Ok(())
}

// ----------------------- //
// -- Private Functions -- //
// ----------------------- //

/// Configures and starts the TCP listener
fn initialise(ip: String, port: u16) -> Result<TcpListener, std::io::Error> {
    let result = TcpListener::bind((ip.as_str(), port));

    match &result {
        Ok(listener) => {
            eprintln!(
                "Server listening on {}",
                listener.local_addr().expect("Failed to get local address")
            );
        }
        Err(e) => {
            panic!("Failed to bind to {}:{}. Error: {}", &ip, port, e);
        }
    }

    result
}

/// Handles a new connection request.
fn handle_connection(mut stream: TcpStream) -> Result<(), std::io::Error> {
    // Get metadata about the connection
    let addr = extract_connection_metadata(&stream);

    println!("New connection from {}:{}", addr.ip(), addr.port());

    // Read the connection stream
    let mut buffer = [0; BUFFER_SIZE];
    loop {
        match stream.read(&mut buffer) {
            Ok(0) => {
                handle_client_disconnect(addr);
                break;
            }
            Ok(n) => {
                let received_data = String::from_utf8_lossy(&buffer[..n]);

                // TODO: Process data according to protocol
                // TODO: Actually send the data to other clients
                // DEBUG: print to stderr for now

                eprintln!("[{}:{}] {}", addr.ip(), addr.port(), received_data);
            }
            Err(e) => {
                eprintln!("Error: {}", e);
                break;
            }
        }
    }

    Ok(())
}

// ----------- //
// -- Other -- //
// ----------- //

// TODO: Consider moving this to another file/module

fn extract_connection_metadata(stream: &TcpStream) -> std::net::SocketAddr {
    stream.peer_addr().expect("Failed to get peer address")
}

fn handle_client_disconnect(addr: std::net::SocketAddr) {
    println!("Client {}:{} disconnected.", addr.ip(), addr.port());
}
