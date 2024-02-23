mod codes;

fn main() {
    let color = codes::get_random_color();
    let noun = codes::get_random_noun();

    println!("{} {}", color, noun)
}
