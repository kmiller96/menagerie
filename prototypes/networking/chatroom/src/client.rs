const BUFFER_SIZE: usize = 512;

// ---------------------- //
// -- Public Functions -- //
// ---------------------- //

#[allow(unused_imports)]
use std::{
    io::{Read, Write},
    net::TcpStream,
};

pub fn run_client(ip: String, port: u16) -> Result<(), std::io::Error> {
    match TcpStream::connect((ip.as_str(), port)) {
        Ok(mut stream) => {
            println!("Connected to server at {}:{}", ip, port);

            // Send a message
            let message = b"Hello from client!";
            stream.write_all(message).unwrap();

            // Read the response
            stream.set_read_timeout(Some(std::time::Duration::from_millis(2000)))?;

            let mut buffer = [0; BUFFER_SIZE];
            match stream.read(&mut buffer) {
                Ok(n) => {
                    let received_data = String::from_utf8_lossy(&buffer[..n]);
                    println!("Received: {}", received_data);
                }
                Err(e) => {
                    eprintln!("Failed to read from server: {}", e);
                }
            }

            Ok(())
        }
        Err(e) => {
            eprintln!(
                "Failed to connect to server at {}:{}. Error: {}",
                ip, port, e
            );

            Err(e)
        }
    }
}

// ----------------------- //
// -- Private Functions -- //
// ----------------------- //

// TODO
