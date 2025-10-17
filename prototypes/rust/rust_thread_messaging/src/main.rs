use std::sync::mpsc;
use std::thread;
use std::time::Duration;

#[derive(Debug)]
struct Message;

impl Message {
    fn new() -> Self {
        Message {}
    }
}

fn main() {
    let (tx, rx) = mpsc::channel::<Message>();

    println!("Spawning thread to send a message...");
    thread::spawn(move || {
        thread::sleep(Duration::from_secs(1));

        let message = Message::new();
        tx.send(message).unwrap();
    });

    println!("Waiting for message...");
    println!("Message received: {:?}", rx.recv().unwrap());
}
