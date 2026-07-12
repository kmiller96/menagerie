//! The calculator program.

/// Calculator program.
pub struct Calculator {
    total: f64,
}

impl Calculator {
    /// Creates a new instance of the application.
    pub fn new() -> Self {
        Calculator { total: 0.0 }
    }

    /// Adds a number to the running total.
    pub fn add(&mut self, x: f64) -> f64 {
        self.total += x;
        self.total
    }

    /// Subtracts a number from the running total.
    pub fn subtract(&mut self, x: f64) -> f64 {
        self.total -= x;
        self.total
    }

    /// Multiplies the running total by a number.
    pub fn multiply(&mut self, x: f64) -> f64 {
        self.total *= x;
        self.total
    }

    /// Divides the running total by a number.
    pub fn divide(&mut self, x: f64) -> f64 {
        if x == 0.0 {
            eprintln!("Error: Division by zero");
            return self.total;
        }
        self.total /= x;
        self.total
    }

    /// Sets the running total to a specific number.
    pub fn set(&mut self, x: f64) -> f64 {
        self.total = x;
        self.total
    }

    /// Gets the current total.
    pub fn total(&self) -> f64 {
        self.total
    }
}
