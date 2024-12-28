use std::io;
use std::thread;
use std::time;

use ratatui;

fn main() -> io::Result<()> {
    let mut terminal = ratatui::init();

    terminal.clear()?;
    terminal.draw(|frame| {
        frame.render_widget("Hello World!", frame.area());
    })?;

    thread::sleep(time::Duration::from_secs(2));

    ratatui::restore();
    Ok(())
}
