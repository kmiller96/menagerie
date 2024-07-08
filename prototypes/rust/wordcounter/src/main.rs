use std::fs;

mod algorithm;
mod cli;
mod formatter;

fn main() {
    let args = cli::parse();

    let content = match fs::read_to_string(args.input) {
        Ok(s) => s,
        Err(e) => {
            println!("Unable to read file. {e:?}");
            std::process::exit(1);
        }
    };

    let counts = algorithm::count_words(content);
    let output = formatter::fmt(counts);

    match fs::write(args.output, output) {
        Ok(v) => v,
        Err(e) => {
            println!("Unable to write the output file. {e:?}");
            std::process::exit(1);
        }
    };
}
