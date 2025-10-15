use std::{
    io::{Read, Write},
    net::{TcpListener, TcpStream},
};

/// Handles a new client connection
///
/// While developing, it simply echos back the input.
#[allow(unused_mut)] // TODO: Remove when implemented
fn handle_new_connection(mut stream: TcpStream) {
    println!("New client: {}", stream.peer_addr().unwrap());

    let mut buffer = [0; 1024];
    loop {
        match stream.read(&mut buffer) {
            Ok(0) => break, // Connection closed
            Ok(n) => {
                println!(
                    "Received from {}: {}",
                    stream.peer_addr().unwrap(),
                    String::from_utf8_lossy(&buffer[0..n])
                );

                // Echo back the received data
                match stream.write_all(&buffer[0..n]) {
                    Ok(_) => {}
                    Err(e) => {
                        eprintln!(
                            "Failed to send data to {}: {}",
                            stream.peer_addr().unwrap(),
                            e
                        );
                        break;
                    }
                }
            }
            Err(e) => {
                eprintln!("Failed to read from {}: {}", stream.peer_addr().unwrap(), e);
                break;
            }
        }
    }

    println!("Disconnected client: {}", stream.peer_addr().unwrap());
}

/// Starts the TCP server
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
        handle_new_connection(stream.unwrap());
    }

    // Return
    return;
}
