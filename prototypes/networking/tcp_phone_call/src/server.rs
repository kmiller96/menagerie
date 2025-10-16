use std::{
    io::{Read, Write},
    net::{Shutdown, TcpListener, TcpStream},
};

// ---------------------- //
// -- Public Functions -- //
// ---------------------- //

/// Starts the TCP server
pub fn run_server(ip: String, port: u16) -> Result<(), std::io::Error> {
    let listener = initialise(ip, port)?;

    for stream in listener.incoming() {
        handle_connection(stream)?;
    }

    Ok(())
}

// ----------------------- //
// -- Private Functions -- //
// ----------------------- //

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
            eprintln!("Error binding to {}:{} - {}", &ip, port, e);
        }
    }

    result
}

/// Handles a new client connection
fn handle_connection(stream: Result<TcpStream, std::io::Error>) -> Result<(), std::io::Error> {
    match stream {
        Ok(data) => {
            let client_address = data.peer_addr().unwrap();
            eprintln!("New client: {}", client_address);

            match authorize_connection(&client_address) {
                ConnectionAction::Accept => {
                    eprintln!("Accepted: {}", client_address);
                    handle_stream(data)
                }
                ConnectionAction::Reject => {
                    eprintln!("Rejected: {}", client_address);
                    match data.shutdown(Shutdown::Both) {
                        Ok(_) => {}
                        Err(e) => {
                            eprintln!("Failed to close connection: {}", e);
                        }
                    }
                }
            };

            println!("Disconnected client: {}", client_address);
        }
        Err(e) => {
            eprintln!("Failed to accept connection: {}", e);
            return Err(e);
        }
    }

    Ok(())
}

/// Handles communication with a connected client
fn handle_stream(mut stream: TcpStream) {
    let client_address = stream.peer_addr().unwrap();

    let mut buffer = [0; 1024];
    loop {
        match stream.read(&mut buffer) {
            Ok(n) => {
                if n == 0 {
                    break; // Connection closed
                };

                // TODO: Handle case where data is larger than buffer

                match stream.write_all(&buffer[0..n]) {
                    Ok(_) => {}
                    Err(e) => {
                        eprintln!("Failed to send data to {}: {}", client_address, e);
                        break;
                    }
                }
            }
            Err(e) => {
                eprintln!("Failed to read from {}: {}", client_address, e);
                break;
            }
        }
    }
}

// ----------- //
// -- Other -- //
// ----------- //

// TODO: Move this to a separate module

enum ConnectionAction {
    Accept,
    Reject,
}

/// Authorizes a new connection
///
/// Currently random to test, but should be replaced with real logic.
#[allow(unused_variables)]
fn authorize_connection(client_address: &std::net::SocketAddr) -> ConnectionAction {
    if rand::random_bool(0.5) {
        return ConnectionAction::Accept;
    } else {
        return ConnectionAction::Reject;
    }
}
