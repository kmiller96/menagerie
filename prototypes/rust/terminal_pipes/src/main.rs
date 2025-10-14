mod constants;

use std::io::{stdout, Write};

use crossterm::{
    event, execute,
    style::{Color, Print, ResetColor, SetBackgroundColor, SetForegroundColor},
    ExecutableCommand,
};

fn main() -> std::io::Result<()> {
    // using the macro
    execute!(
        stdout(),
        SetForegroundColor(Color::Blue),
        SetBackgroundColor(Color::Red),
        Print("Styled text here."),
        ResetColor
    )?;

    // or using functions
    stdout()
        .execute(SetForegroundColor(Color::Blue))?
        .execute(SetBackgroundColor(Color::Red))?
        .execute(Print("Styled text here."))?
        .execute(ResetColor)?;

    Ok(())
}

// fn main() {
//     println!("Hello, world!");
//     println!("{}", constants::Characters::HorizontalBar.as_str());
//     println!("{}", constants::Characters::VerticalBar.as_str());
//     println!("{}", constants::Characters::RightDown.as_str());
//     println!("{}", constants::Characters::LeftDown.as_str());
//     println!("{}", constants::Characters::RightUp.as_str());
//     println!("{}", constants::Characters::LeftUp.as_str());
//     println!("{}", constants::Characters::TeeLeft.as_str());
//     println!("{}", constants::Characters::TeeRight.as_str());
//     println!("{}", constants::Characters::TeeUp.as_str());
//     println!("{}", constants::Characters::TeeDown.as_str());
// }
