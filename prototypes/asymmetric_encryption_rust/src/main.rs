use std::{fs, path::PathBuf};

use base64::{engine::general_purpose, Engine as _};
use clap::Parser;
use rand::rngs::OsRng;
use rsa::{
    pkcs1::{
        DecodeRsaPrivateKey, DecodeRsaPublicKey, EncodeRsaPrivateKey, EncodeRsaPublicKey,
        LineEnding,
    },
    pkcs1v15::Pkcs1v15Encrypt,
    traits::PublicKeyParts,
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
    Encrypt {
        key: PathBuf,
        input: PathBuf,
        output: Option<PathBuf>,
    },

    /// Decrypts a file with the given key
    Decrypt {
        key: PathBuf,
        input: PathBuf,
        output: Option<PathBuf>,
    },
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

fn encrypt_file(key: PathBuf, input: PathBuf, output: Option<PathBuf>) {
    let public_pem = fs::read_to_string(&key).expect("failed to read public key");
    let public_key = RsaPublicKey::from_pkcs1_pem(&public_pem).expect("invalid public key PEM");

    let plaintext = fs::read(&input).expect("failed to read input file");
    let max_chunk_len = public_key.size().saturating_sub(11);
    assert!(
        max_chunk_len > 0,
        "public key size too small for encryption"
    );

    let mut rng = OsRng;
    let mut ciphertext = Vec::new();

    for chunk in plaintext.chunks(max_chunk_len) {
        let encrypted = public_key
            .encrypt(&mut rng, Pkcs1v15Encrypt, chunk)
            .expect("failed to encrypt chunk");
        ciphertext.extend_from_slice(&encrypted);
    }

    match output {
        Some(ref path) => {
            fs::write(&path, &ciphertext).expect("failed to write encrypted file");
        }
        None => println!("{}", general_purpose::STANDARD.encode(&ciphertext)),
    }
}

fn decrypt_file(key: PathBuf, input: PathBuf, output: Option<PathBuf>) {
    let private_pem = fs::read_to_string(&key).expect("failed to read private key");
    let private_key = RsaPrivateKey::from_pkcs1_pem(&private_pem).expect("invalid private key PEM");

    let key_size = private_key.size();
    let mut ciphertext = fs::read(&input).expect("failed to read input file");

    if ciphertext.len() % key_size != 0 {
        // Accept base64-encoded ciphertext if the file isn't aligned to key size.
        let encoded = fs::read_to_string(&input).expect("failed to read base64 input file");
        ciphertext = general_purpose::STANDARD
            .decode(encoded.trim())
            .expect("failed to decode base64 ciphertext");
    }

    assert!(
        ciphertext.len() % key_size == 0,
        "ciphertext length must be a multiple of key size"
    );

    let mut plaintext = Vec::new();
    for chunk in ciphertext.chunks(key_size) {
        let decrypted = private_key
            .decrypt(Pkcs1v15Encrypt, chunk)
            .expect("failed to decrypt chunk");
        plaintext.extend_from_slice(&decrypted);
    }

    match output {
        Some(ref path) => {
            fs::write(&path, &plaintext).expect("failed to write decrypted file");
        }
        None => {
            println!("{}", String::from_utf8_lossy(&plaintext));
        }
    }
}

// ------------------ //
// -- Main Routine -- //
// ------------------ //

fn main() {
    let args = Cli::parse();

    match args.command {
        Commands::Generate { public, private } => generate_key(public, private),
        Commands::Encrypt { key, input, output } => encrypt_file(key, input, output),
        Commands::Decrypt { key, input, output } => decrypt_file(key, input, output),
    }
}
