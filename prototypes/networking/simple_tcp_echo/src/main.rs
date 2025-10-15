use std::io::{BufRead, BufReader};
use std::net::{TcpListener, TcpStream};

fn handle_client(stream: TcpStream) {
    eprintln!("New client: {}", stream.peer_addr().unwrap());

    let mut reader = BufReader::new(stream);
    let mut buffer = String::new();

    reader.read_line(&mut buffer).unwrap();

    let response = buffer.trim();

    eprintln!("Received: {}", response);
    println!("{}", response);
}

fn main() -> std::io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:8000")?;

    eprintln!("Server listening on {}", listener.local_addr()?);

    for stream in listener.incoming() {
        handle_client(stream?);
    }

    Ok(())
}
