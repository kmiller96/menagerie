use std::{
    io::{Read, Write},
    net::TcpStream,
};

// ---------------------- //
// -- Public Functions -- //
// ---------------------- //

// TODO: Figure out why I can't detect server disconnection

pub fn run_client(ip: String, port: u16) -> Result<(), std::io::Error> {
    match TcpStream::connect((ip.as_str(), port)) {
        Ok(mut stream) => {
            println!("Connected to server at {}:{}", ip, port);

            stream.write_all(b"TEST MESSAGE").unwrap();

            let mut buffer = [0; 512]; // Create a buffer to store incoming data
            let bytes_read = stream.read(&mut buffer).unwrap();
            let received_data = String::from_utf8_lossy(&buffer[..bytes_read]);
            println!("Received: {}", received_data);
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
