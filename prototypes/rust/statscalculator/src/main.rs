mod cli;
mod stats;

fn main() {
    // Load the stdin
    let series = match cli::read() {
        Ok(x) => x,
        Err(e) => {
            eprintln!("Invalid user input.");
            eprintln!("{}", e);
            std::process::exit(1)
        }
    };

    // Compute statistics
    let (mean, stddev) = stats::compute(&series);

    // Print to console
    println!("{} {}", mean, stddev);
}
