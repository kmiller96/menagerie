use ratatui;
use std::io;

mod app;
use app::App;

fn main() -> io::Result<()> {
    let mut terminal = ratatui::init();

    let app = App::new();
    let result = app.run(&mut terminal);

    ratatui::restore();
    result
}
