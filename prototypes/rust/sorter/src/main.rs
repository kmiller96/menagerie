//! A CLI program that sorts files into folders based on metadata.
//!
pub mod algorithms;
mod cli;
mod types;

fn main() {
    let args = cli::parse();
    let paths = algorithms::find(&args.path, args.depth).unwrap();
    let targets = algorithms::sort(&paths);

    // TODO: Perform move command on each path
    for i in 0..(targets.clone().len()) {
        let p = &paths[i];
        let t = &targets[i];

        algorithms::migrate(p, t);
    }
}
