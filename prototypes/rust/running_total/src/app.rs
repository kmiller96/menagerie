//! Renders the application.

use std::io::{self, Write};

use crate::calculator::Calculator;

pub struct App {
    calculator: Calculator,
}

impl App {
    /// Creates a new application object.
    pub fn new() -> Self {
        App {
            calculator: Calculator::new(),
        }
    }

    /// Starts the application and runs it in a blocking loop.
    pub fn run(&mut self) {
        eprintln!("Enter text (Press Ctrl+D or Ctrl+Z to finish):");
        io::stderr().flush().unwrap();

        for line in io::stdin().lines() {
            self.handle_stdin(line);
        }
    }

    /// Handles the stdin, processing it appropriately
    fn handle_stdin(&mut self, line: Result<String, io::Error>) {
        // Parse line
        let line = match line {
            Ok(line) => line,
            Err(e) => {
                eprintln!("Error reading line: {}", e);
                return;
            }
        };

        let line = line.trim();

        // Empty line special case
        if line.len() == 0 {
            return;
        }

        // Parse operator
        let operator = line
            .chars()
            .next()
            .expect("Expected at least one character in input");

        // Parse number
        let number = match line[1..].trim().parse::<f64>() {
            Ok(num) => num,
            Err(e) => {
                // Special case: use wants current total
                if line.len() == 1 && operator == '=' {
                    print!("\x1b[1A\x1b[2K"); // Move cursor up and clear line
                    println!("= {}", self.calculator.total());
                    io::stdout().flush().unwrap();
                } else {
                    eprintln!("Error parsing number: {}", e);
                }
                return;
            }
        };

        dbg!(&operator, &number);

        // Handle the operator + number
        match operator {
            '+' => {
                self.calculator.add(number);
            }
            '-' => {
                self.calculator.subtract(number);
            }
            '*' => {
                self.calculator.multiply(number);
            }
            '/' => {
                self.calculator.divide(number);
            }
            '=' => {
                self.calculator.set(number);
            }
            _ => {
                eprintln!("Invalid operator: {}", operator);
            }
        }
    }
}
