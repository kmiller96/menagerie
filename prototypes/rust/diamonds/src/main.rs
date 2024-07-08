use std::env;

/// Creates a diamond with a maximum width supplied of N.
fn main() {
    // -- Collect input args -- //
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        println!("Syntax: [SCRIPT] N");
        std::process::exit(1);
    }

    let width = match &args[1].parse::<u8>() {
        Ok(value) => value.clone(),
        Err(error) => {
            println!("Failed to parse the value! {error:?}");
            std::process::exit(2);
        }
    };

    if width % 2 == 0 {
        println!("Can't create an even diamond. Please supply an odd number.");
        std::process::exit(2);
    };

    // -- Print the diamond -- //
    for i in (1..=(2 * width)).step_by(2) {
        let n = match i {
            i if i <= width => i,
            i if i > width => 2 * width - i,
            _ => panic!("This should never be reached."),
        };

        println!("{}", helpers::create_row(width, n).unwrap());
    }
}

mod helpers {
    /// Creates a "row" of the diamond.
    pub fn create_row(width: u8, n: u8) -> Result<String, &'static str> {
        if n > width {
            return Err("Can't create a row with N > width.");
        } else if (width - n) % 2 != 0 {
            return Err("Can't create an even diamond.");
        }

        let n_body = n as usize;
        let n_whitespace = ((width - n) / 2) as usize;

        let body = String::from("#").repeat(n_body);
        let whitespace = String::from(" ").repeat(n_whitespace);

        let row = format!("{}{}{}", whitespace, body, whitespace);

        Ok(row)
    }
}
