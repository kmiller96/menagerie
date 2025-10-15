use clap::{Parser, Subcommand};

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
        #[arg(short, long, default_value_t = 8000)]
        port: u16,
    },

    /// Start a TCP phone call client
    Client {
        /// Server IP address to connect to
        #[arg(short, long, default_value = "127.0.0.1")]
        ip: String,

        /// Server port to connect to
        #[arg(short, long, default_value_t = 8000)]
        port: u16,
    },
}

// ----------------- //
// -- Subroutines -- //
// ----------------- //

fn run_server(ip: String, port: u16) {
    println!("Starting server at {}:{}", ip, port);
}
fn run_client(ip: String, port: u16) {
    println!("Starting client to connect to {}:{}", ip, port);
}

// ------------------ //
// -- Main Routine -- //
// ------------------ //

fn main() {
    let args = CLI::parse();

    match args.command {
        Commands::Server { ip, port } => {
            run_server(ip, port);
        }
        Commands::Client { ip, port } => {
            run_client(ip, port);
        }
    }
}
