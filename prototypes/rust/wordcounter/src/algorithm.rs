//! Specifies the implementation of the word counting algorithm.

use std::collections::HashMap;

const PUNCTUATION: [char; 7] = ['(', ')', '.', '\'', ',', ';', ':'];

pub fn count_words(content: String) -> HashMap<String, usize> {
    let mut map: HashMap<String, usize> = HashMap::new();

    for word in content.split_whitespace() {
        // TODO: Use Regex here instead of this map-filter logic
        let word = word
            .to_string()
            .to_lowercase()
            .chars()
            .filter(|x| !PUNCTUATION.contains(x))
            .collect();

        let count = match map.get(&word) {
            Some(v) => v.clone(),
            None => 0,
        } as usize;

        map.insert(word, count + 1);
    }

    map
}
