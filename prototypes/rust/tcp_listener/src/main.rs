use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};

fn handle_client(mut stream: TcpStream) {
    let mut buffer = [0; 512]; // A small buffer for reading data

    let bytes_read = stream
        .read(&mut buffer)
        .expect("Failed to read from stream");

    let message = String::from_utf8_lossy(&buffer[..bytes_read]);
    println!("Received: {}", message);

    let response = if message.contains("ping") {
        "pong!\n".to_string()
    } else {
        "unknown command\n".to_string()
    };

    println!("Sending: {}", response.trim());
    stream
        .write_all(response.as_bytes())
        .expect("Failed to write to stream");
}

const ADDR: &str = "127.0.0.1:7878";

fn main() {
    let listener = TcpListener::bind(ADDR).expect("Failed to bind to address");
    println!("Listening on {}", ADDR);

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                println!("New connection: {}", stream.peer_addr().unwrap());
                std::thread::spawn(move || {
                    handle_client(stream);
                });
            }
            Err(e) => {
                eprintln!("Error: {}", e);
            }
        }
    }
}
