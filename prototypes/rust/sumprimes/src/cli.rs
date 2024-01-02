//! Defines the CLI functions
use std::env;

/// Consumes the CLI input to return the number of primes to sum.
pub fn read() -> Result<usize, &'static str> {
    let args: Vec<String> = env::args().skip(1).collect();

    if args.len() != 1 {
        return Err("Invalid number of arguments.");
    }

    let n = match args[0].parse::<usize>() {
        Ok(x) => x,
        Err(_) => return Err("Unable to parse input."),
    };

    Ok(n)
}

pub fn print_usage() {
    println!("USAGE: sumprimes <n primes>");
}
