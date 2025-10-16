use rand::RngCore;
use std::{
    io::{Read, Write},
    net::TcpStream,
};

const BUFFER_SIZE: usize = 512;

// ---------------------- //
// -- Public Functions -- //
// ---------------------- //

// TODO: Figure out why I can't detect server disconnection

pub fn run_client(ip: String, port: u16) -> Result<(), std::io::Error> {
    match TcpStream::connect((ip.as_str(), port)) {
        Ok(mut stream) => {
            println!("Connected to server at {}:{}", ip, port);

            // Send a message
            let mut message = [0; 1000];
            rand::rng().fill_bytes(&mut message);
            stream.write_all(&message).unwrap();

            // Read response
            let mut buffer = [0; BUFFER_SIZE]; // Create a buffer to store incoming data
            loop {
                match stream.read(&mut buffer) {
                    Ok(0) => {
                        println!("Server disconnected.");
                        break;
                    }
                    Ok(n) => {
                        let received_data = String::from_utf8_lossy(&buffer[..n]);
                        println!("Received: {}", received_data);

                        if n < BUFFER_SIZE {
                            // If less data was read than the buffer size, assume the server has finished sending
                            break;
                        }
                    }
                    Err(e) => {
                        eprintln!("Failed to read from server: {}", e);
                    }
                }
            }
        }
        Err(e) => {
            eprintln!("Failed to connect to server: {}", e);
        }
    };

    println!("Client disconnecting.");
    Ok(())
}

// ------------------------- //
// -- Private Connections -- //
// ------------------------- //

// TODO
