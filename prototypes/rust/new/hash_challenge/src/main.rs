use clap::Parser;

use hex;
use sha2::{Digest, Sha256};

// ---------- //
// -- Args -- //
// ---------- //

/// Simulates proof-of-work by finding a hash with a specified number of leading zeros.
#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Args {
    difficulty: u32,
}

// ----------------- //
// -- Subroutines -- //
// ----------------- //

fn parse_args() -> u32 {
    // Parse CLI input
    let args = Args::parse();
    let difficulty = args.difficulty;

    // Sanitise input
    if difficulty == 0 {
        eprintln!("Error: Difficulty must be greater than zero.");
        std::process::exit(1);
    }

    // Return difficulty
    difficulty
}

fn find_valid_hash(difficulty: u32) -> String {
    let hash: String;
    let mut nonce: u64 = 0;

    loop {
        // Compute hash of nonce
        let candidate = hex::encode(Sha256::digest(nonce.to_le_bytes()));

        // Check if hash meets difficulty
        let leading_zeros = candidate.chars().take_while(|&c| c == '0').count() as u32;

        if leading_zeros < difficulty {
            nonce += 1;
            continue;
        } else {
            println!("Iterations: {}", nonce);
            hash = candidate;
            break;
        }
    }

    hash
}

// ------------------ //
// -- Main Routine -- //
// ------------------ //

fn main() {
    let difficulty = parse_args();
    let hash = find_valid_hash(difficulty);
    println!("Valid Hash: {}", hash);
}
