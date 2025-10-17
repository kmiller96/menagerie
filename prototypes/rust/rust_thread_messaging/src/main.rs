use std::sync::mpsc;
use std::thread;
use std::time::Duration;

#[derive(Debug, Clone)]
struct Message {
    content: String,
}

impl Message {
    pub fn new(content: String) -> Self {
        Message { content }
    }

    pub fn content(&self) -> &str {
        &self.content
    }
}

fn main() {
    let (tx, rx) = mpsc::channel::<Message>();

    println!("Spawning thread #1 to send a message...");
    let tx1 = tx.clone();
    thread::spawn(move || {
        thread::sleep(Duration::from_secs(1));

        let message = Message::new("Hello from thread #1".to_string());
        tx1.send(message).unwrap();
        println!("Message sent from thread #1");
    });

    println!("Spawning thread #2 to send a message...");
    let tx2 = tx.clone();
    thread::spawn(move || {
        thread::sleep(Duration::from_secs(2));

        let message = Message::new("Hello from thread #2".to_string());
        tx2.send(message).unwrap();
        println!("Message sent from thread #2");
    });

    println!("Waiting for message...");
    println!("Message received: {:?}", rx.recv().unwrap().content());
    println!("Message received: {:?}", rx.recv().unwrap().content());
}
