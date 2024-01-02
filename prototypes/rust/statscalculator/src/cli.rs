use std::{
    env,
    io::{self, Read},
    num::ParseFloatError,
};

pub fn read() -> Result<Vec<f64>, &'static str> {
    // Attempt to read in the CLI input from many locations
    let series: Vec<String> = match read_positional_args() {
        Some(x) => Ok(x),
        None => match read_stdin() {
            Some(x) => Ok(split_string_to_vector_series(x)),
            None => Err("No input supplied"),
        },
    }?;

    // Parse into a vector
    let series = match convert_strings_to_floats(series) {
        Ok(v) => Ok(v),
        Err(_) => Err("Unable to parse user input"),
    }?;

    // If all succeeds, return Ok(series)
    Ok(series)
}

fn read_positional_args() -> Option<Vec<String>> {
    let args: Vec<String> = env::args().skip(1).collect();

    if &args.len() == &0 {
        None
    } else {
        Some(args)
    }
}

fn read_stdin() -> Option<String> {
    let mut stdin = io::stdin();
    let mut buffer = String::new();

    stdin.read_to_string(&mut buffer).unwrap();

    Some(buffer)
}

fn split_string_to_vector_series(s: String) -> Vec<String> {
    s.replace("\n", " ") // Convert newlines to simple whitespace
        .split(" ") // Split on simple whitespace
        .filter(|x| x != &"") // Remove empty elements
        .map(|x| x.to_string())
        .collect()
}

fn convert_strings_to_floats(s: Vec<String>) -> Result<Vec<f64>, ParseFloatError> {
    s.into_iter().map(|x| x.parse::<f64>()).collect()
}
