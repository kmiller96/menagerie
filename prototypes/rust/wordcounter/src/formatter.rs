//! Contains the formatting function for the output.

use std::collections::HashMap;

pub fn fmt(counts: HashMap<String, usize>) -> String {
    let mut output = String::new();

    for (k, v) in counts.iter() {
        output.push_str(&format!("{} {}\n", k, v))
    }

    output
}
