mod client;
mod server;

use clap::{Parser, Subcommand};

const DEFAULT_PORT: u16 = 2428;

// -------------------- //
// -- CLI Definition -- //
// -------------------- //

/// TCP Calling Software
#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct CLI {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Start the TCP phone call server
    Server {
        /// IP address to bind the server to
        #[arg(short, long, default_value = "127.0.0.1")]
        ip: String,

        /// Port to bind the server to
        #[arg(short, long, default_value_t = DEFAULT_PORT)]
        port: u16,
    },

    /// Start a TCP phone call client
    Client {
        /// Server IP address to connect to
        ip: Option<String>,

        /// Server port to connect to
        #[arg(short, long, default_value_t = DEFAULT_PORT)]
        port: u16,
    },
}

// ------------------ //
// -- Main Routine -- //
// ------------------ //

fn main() {
    let args = CLI::parse();

    let result = match args.command {
        Commands::Server { ip, port } => server::run_server(ip, port),
        Commands::Client { ip, port } => {
            client::run_client(ip.unwrap_or(String::from("127.0.0.1")), port)
        }
    };

    if let Err(e) = result {
        eprintln!("Error: {}", e);
    }
}
