mod cli;
mod primes;

fn main() {
    let n = match cli::read() {
        Ok(x) => x,
        Err(e) => {
            println!("{}", e);
            cli::print_usage();
            std::process::exit(1);
        }
    };

    let sum = primes::sum_primes(&n);

    println!("{}", sum)
}
