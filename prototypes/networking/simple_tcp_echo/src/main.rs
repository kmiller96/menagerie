use std::io::{Read, Write};
use std::net::{TcpListener, TcpStream};

fn handle_client(mut stream: TcpStream) {
    let peer = stream.peer_addr().unwrap();
    eprintln!("New client: {}", peer);

    let mut buffer = [0; 1028];
    match stream.read(&mut buffer) {
        Ok(n) => {
            // Read buffer into string
            let content = String::from_utf8_lossy(&buffer[..n]);
            let message = content.trim();

            // Log raw message to stdout
            eprintln!("Received: {}", message);
            println!("{}", message);

            // Exit on "exit" message
            if message == "exit" {
                eprintln!("Client requested exit: {}", peer);
            } else {
                // Echo message back to client and log.
                eprintln!("Sent: {}", message);
                stream
                    .write((message.to_owned() + "\r\n").as_bytes())
                    .unwrap();
            }
        }
        Err(err) => {
            panic!("{}", err);
        }
    }

    eprintln!("Client disconnected: {}", peer);
}

fn main() -> std::io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:8000")?;

    eprintln!("Server listening on {}", listener.local_addr()?);

    for stream in listener.incoming() {
        handle_client(stream?);
    }

    Ok(())
}
