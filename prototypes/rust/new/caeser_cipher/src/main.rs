use clap::{Parser, Subcommand};
use clap_stdin::FileOrStdin;

// --------- //
// -- CLI -- //
// --------- //

/// Program to encrypt and decrypt text using a Caesar cipher.
#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand, Debug)]
enum Commands {
    /// Encrypts text using a Caesar cipher.
    Encrypt {
        /// The input file to use, or stdin if not present
        input: FileOrStdin<String>,

        /// The secret for the cipher. Indicates how many letters to shift by.
        #[arg(short, long)]
        secret: u32,
    },
    /// Encrypts text using a Caesar cipher.
    Decrypt {
        /// The input file to use, or stdin if not present
        input: FileOrStdin<String>,

        /// The secret for the cipher. Indicates how many letters to shift by.
        #[arg(short, long)]
        secret: u32,
    },
}

// ----------------- //
// -- Subroutines -- //
// ----------------- //

fn encrypt(text: String, secret: u32) -> String {
    let mut output = String::new();

    for c in text.chars() {
        let shifted = c as u32 + secret;
        output.push(shifted as u8 as char);
    }

    dbg!(&output);
    output
}

fn decrypt(text: String, secret: u32) -> String {
    let mut output = String::new();

    for c in text.chars() {
        let unshifted = c as u32 - secret;
        output.push(unshifted as u8 as char);
    }

    dbg!(&output);
    output
}

fn try_parse_input(input: &FileOrStdin<String>) -> String {
    let content = input.clone().contents();
    match content {
        Ok(c) => c,
        Err(e) => {
            eprintln!("Error reading input: {}", e);
            std::process::exit(1);
        }
    }
}

fn try_parse_secret(secret: &u32) -> u32 {
    *secret % 26
}

// ------------------ //
// -- Main Program -- //
// ------------------ //

fn main() {
    let args = Cli::parse();
    dbg!(&args);

    match &args.command {
        Commands::Encrypt { input, secret } => {
            let content = try_parse_input(input);
            let secret = try_parse_secret(secret);
            encrypt(content, secret)
        }
        Commands::Decrypt { input, secret } => {
            let content = try_parse_input(input);
            let secret = try_parse_secret(secret);
            decrypt(content, secret)
        }
    };
}
