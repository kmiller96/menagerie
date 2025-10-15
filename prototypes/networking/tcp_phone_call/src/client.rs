use std::net::TcpStream;

pub fn run_client(ip: String, port: u16) {
    match TcpStream::connect((ip.as_str(), port)) {
        Ok(stream) => {
            println!("Connected to server at {}:{}", ip, port);
        }
        Err(e) => {
            eprintln!("Failed to connect to server: {}", e);
        }
    };

    println!("Client disconnecting.");
}
