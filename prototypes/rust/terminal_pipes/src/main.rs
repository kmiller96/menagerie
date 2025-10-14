mod constants;
mod graphics;

use crossterm::cursor;

use graphics::Graphics;

fn main() -> std::io::Result<()> {
    let mut graphics = Graphics::new();

    graphics.clear()?;
    graphics.print(0, 1, constants::Characters::HorizontalBar.as_str())?;
    graphics.print(0, 2, constants::Characters::VerticalBar.as_str())?;
    graphics.print(0, 3, constants::Characters::RightDown.as_str())?;
    graphics.print(0, 4, constants::Characters::LeftDown.as_str())?;
    graphics.print(0, 5, constants::Characters::RightUp.as_str())?;
    graphics.print(0, 6, constants::Characters::LeftUp.as_str())?;
    graphics.print(0, 7, constants::Characters::TeeLeft.as_str())?;
    graphics.print(0, 8, constants::Characters::TeeRight.as_str())?;
    graphics.print(0, 9, constants::Characters::TeeUp.as_str())?;
    graphics.print(0, 10, constants::Characters::TeeDown.as_str())?;
    graphics.queue(cursor::MoveTo(0, 12))?;

    graphics.flush()?;

    Ok(())
}
