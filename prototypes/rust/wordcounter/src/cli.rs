use std::{env, path::PathBuf};

/// Parses the CLI input and returns the arguments in a structured format.
pub fn parse() -> ProgramArgs {
    let args: Vec<String> = env::args().collect();

    ProgramArgs {
        input: PathBuf::from(&args[1]),
        output: PathBuf::from(&args[2]),
    }
}

#[derive(Debug)]
pub struct ProgramArgs {
    pub input: PathBuf,
    pub output: PathBuf,
}
