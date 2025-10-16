// ---------------------- //
// -- Public Functions -- //
// ---------------------- //

use std::net::TcpStream;

pub fn run_client(ip: String, port: u16) -> Result<(), std::io::Error> {
    match TcpStream::connect((ip.as_str(), port)) {
        Ok(_stream) => {
            println!("Connected to server at {}:{}", ip, port);

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
