use std::io;
use std::io::Write;
use std::thread;
use std::time::Duration;

use crossterm::{
    cursor, execute, queue, style,
    terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen},
};

fn main() -> Result<(), ()> {
    let mut stdout = io::stdout();

    setup(&mut stdout).unwrap();
    let result = run(&mut stdout);
    teardown(&mut stdout).unwrap();

    result
}

/** Sets up the terminal. */
fn setup(stdout: &mut io::Stdout) -> io::Result<()> {
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

/** Runs the main program. */
fn run(stdout: &mut io::Stdout) -> Result<(), ()> {
    // Queue the events
    match queue!(stdout, cursor::MoveTo(1, 1), style::Print("Hello!")) {
        Ok(_) => (),
        Err(_) => return Err(()),
    };

    // Flush the events
    match stdout.flush() {
        Ok(_) => (),
        Err(_) => return Err(()),
    };

    // DEBUG: Wait for 2 seconds
    thread::sleep(Duration::from_secs(2));

    Ok(())
}
