use std::io;

use crossterm::terminal::{disable_raw_mode, enable_raw_mode};
use ratatui;

mod app;
use app::App;

fn main() -> io::Result<()> {
    let mut terminal = ratatui::init();
    enable_raw_mode()?;

    let app = App::new();
    let result = app.run(&mut terminal);

    disable_raw_mode()?;
    ratatui::restore();

    result
}
