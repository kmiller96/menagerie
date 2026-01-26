use std::{fs, path::PathBuf};

use clap::Parser;
use rand::rngs::OsRng;
use rsa::{
    pkcs1::{EncodeRsaPrivateKey, EncodeRsaPublicKey, LineEnding},
    RsaPrivateKey, RsaPublicKey,
};

// -------------------- //
// -- CLI Definition -- //
// -------------------- //

#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Parser, Debug)]
enum Commands {
    /// Generates a new encryption key
    Generate {
        /// Path to save the public key
        public: PathBuf,

        /// Path to save the private key
        private: PathBuf,
    },

    /// Encrypts a file with the given key
    Encrypt { key: PathBuf, path: PathBuf },

    /// Decrypts a file with the given key
    Decrypt { key: PathBuf, path: PathBuf },
}

// ----------------- //
// -- Subroutines -- //
// ----------------- //

fn generate_key(public: PathBuf, private: PathBuf) {
    // Initialize RSA key pair
    let mut rng = OsRng;
    let bits = 2048;

    let private_key = RsaPrivateKey::new(&mut rng, bits).expect("failed to generate a key");
    let public_key = RsaPublicKey::from(&private_key);

    // Save keys to files
    let private_pem = private_key
        .to_pkcs1_pem(LineEnding::LF)
        .expect("failed to encode private key as PEM");
    let public_pem = public_key
        .to_pkcs1_pem(LineEnding::LF)
        .expect("failed to encode public key as PEM");

    fs::write(&private, private_pem.as_bytes()).expect("failed to write private key");
    fs::write(&public, public_pem.as_bytes()).expect("failed to write public key");
}

fn encrypt_file(key: PathBuf, path: PathBuf) {
    // Placeholder for file encryption logic
    println!(
        "Encrypting file at {} with key {}",
        path.display(),
        key.display()
    );
}

fn decrypt_file(key: PathBuf, path: PathBuf) {
    // Placeholder for file decryption logic
    println!(
        "Decrypting file at {} with key {}",
        path.display(),
        key.display()
    );
}

// ------------------ //
// -- Main Routine -- //
// ------------------ //

fn main() {
    let args = Cli::parse();

    match args.command {
        Commands::Generate { public, private } => generate_key(public, private),
        Commands::Encrypt { key, path } => encrypt_file(key, path),
        Commands::Decrypt { key, path } => decrypt_file(key, path),
    }
}
