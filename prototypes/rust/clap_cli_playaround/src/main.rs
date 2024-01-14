use clap::Parser;

/// CLI interface
#[derive(Parser, Debug)]
#[command(about = "Add two numbers together")]
struct Args {
    #[arg(help = "First number to add")]
    a: i32,
    #[arg(help = "Second number to add")]
    b: i32,
}

/// CLI interface to add two numbers together
///
/// Just a practice project to learn the clap package.
fn main() {
    let args = Args::parse();
    println!("{}", args.a + args.b);
}
