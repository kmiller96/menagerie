use std::thread;
use std::time::Duration;

const N_THREADS: usize = 10;

fn main() {
    // Create thread collection
    let mut threads = vec![];

    // Create slow threads
    for i in 1..=N_THREADS {
        threads.push(thread::spawn(move || {
            thread::sleep(Duration::from_millis((N_THREADS - i) as u64 * 200));
            println!("Thread {i} done!");
        }));
    }

    // Quickly print from the main thread
    for i in 1..=5 {
        println!("hi number {i} from the main thread!");
    }

    // Join all the threads
    for handle in threads {
        handle.join().unwrap();
    }

    // Print a final completion message
    println!("All threads completed!");
}
