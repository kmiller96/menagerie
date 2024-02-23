//! Collection of codes used to generate codenames

use rand::random;

const COLORS: [&str; 10] = [
    "Green", "Red", "Blue", "Yellow", "Orange", "Purple", "Black", "White", "Brown", "Pink",
];

const NOUNS: [&str; 10] = [
    "Apple",
    "Banana",
    "Carrot",
    "Dog",
    "Elephant",
    "Frog",
    "Giraffe",
    "Horse",
    "Iguana",
    "Jellyfish",
];

fn get_random_value<'a>(values: &'a [&str]) -> &'a str {
    let index = random::<usize>() % values.len();
    values[index]
}

pub fn get_random_color() -> &'static str {
    get_random_value(&COLORS)
}

pub fn get_random_noun() -> &'static str {
    get_random_value(&NOUNS)
}
