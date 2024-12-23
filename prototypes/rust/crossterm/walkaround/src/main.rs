mod app;

use anyhow::Result;
use crossterm::{
    execute,
    terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen},
};
use std::io;

use app::App;

fn main() -> Result<()> {
    let mut stdout = io::stdout();

    setup(&mut stdout).unwrap();

    let mut app = App::init();
    let result = app.run();

    teardown(&mut stdout).unwrap();

    result
}

/** Sets up the terminal. */
fn setup(stdout: &mut io::Stdout) -> Result<()> {
    execute!(stdout, EnterAlternateScreen)?;
    enable_raw_mode()?;

    Ok(())
}

/** Tears down the terminal. */
fn teardown(stdout: &mut io::Stdout) -> io::Result<()> {
    disable_raw_mode()?;
    execute!(stdout, LeaveAlternateScreen)?;

    Ok(())
}
