mod constants;

fn main() {
    println!("Hello, world!");
    println!("{}", constants::Characters::HorizontalBar.as_str());
    println!("{}", constants::Characters::VerticalBar.as_str());
    println!("{}", constants::Characters::RightDown.as_str());
    println!("{}", constants::Characters::LeftDown.as_str());
    println!("{}", constants::Characters::RightUp.as_str());
    println!("{}", constants::Characters::LeftUp.as_str());
    println!("{}", constants::Characters::TeeLeft.as_str());
    println!("{}", constants::Characters::TeeRight.as_str());
    println!("{}", constants::Characters::TeeUp.as_str());
    println!("{}", constants::Characters::TeeDown.as_str());
}
