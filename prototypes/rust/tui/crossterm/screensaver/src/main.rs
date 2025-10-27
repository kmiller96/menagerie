use std::{
    io::{self, Write},
    thread, time,
};

use crossterm::{cursor, execute, queue, style, terminal};

const FPS: u128 = 5;
const TICK_DURATION: u128 = 1000 / FPS;

// ------------------ //
// -- Main Routine -- //
// ------------------ //

fn main() -> io::Result<()> {
    // TEMP: for testing only
    let mut counter = 0;

    // Setup stdout
    let mut stdout = initialise()?;

    // Run main loop
    loop {
        // Start loop timer
        let start = time::SystemTime::now();

        // Queue up drawing commands
        queue!(
            stdout,
            terminal::Clear(terminal::ClearType::All),
            cursor::MoveTo(0, 0),
            style::Print(format!("Counter: {}\n", counter))
        )?;

        // Flush all queued commands
        stdout.flush()?;

        // Wait as long as required to stick to desired FPS
        let elapsed = start.elapsed().unwrap().as_millis();

        if elapsed < TICK_DURATION {
            let delta = TICK_DURATION - elapsed;
            let duration = time::Duration::from_millis(delta as u64);
            thread::sleep(duration);
        }

        // TEMP: For testing
        if counter >= 100 {
            break;
        } else {
            counter += 1;
        }
    }

    Ok(())
}

// --------------- //
// -- Utilities -- //
// --------------- //

/// Initialises the STDOUT to be writable for crossterm.
fn initialise() -> io::Result<io::Stdout> {
    let mut stdout = io::stdout();

    execute!(
        stdout,
        crossterm::terminal::EnterAlternateScreen,
        style::SetForegroundColor(style::Color::Green)
    )?;

    Ok(stdout)
}
