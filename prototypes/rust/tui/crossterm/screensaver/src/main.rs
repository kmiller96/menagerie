use std::{
    io::{self, Write},
    thread, time,
};

use crossterm::{cursor, execute, queue, style, terminal};

const FPS: u128 = 5;
const TICK_DURATION: u128 = 1000 / FPS;

// ----------- //
// -- Enums -- //
// ----------- //

enum ProgramState {
    Running,
    Exiting,
}

// ------------------ //
// -- Main Routine -- //
// ------------------ //

fn main() -> io::Result<()> {
    // TEMP: for testing only
    let mut counter = 0;

    // Setup stdout
    let mut stdout = initialise()?;

    // Run main loop
    rate_limit(move || {
        // Queue up drawing commands
        queue!(
            stdout,
            terminal::Clear(terminal::ClearType::All),
            cursor::MoveTo(0, 0),
            style::Print(format!("Counter: {}\n", counter))
        )?;

        // Flush all queued commands
        stdout.flush()?;

        // TEMP: For testing
        if counter >= 100 {
            return Ok(ProgramState::Exiting);
        } else {
            counter += 1;
        }

        // Return ok
        Ok(ProgramState::Running)
    })?;

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

/// Rate limits the execution of a function to a specified frames-per-second.
fn rate_limit(mut func: impl FnMut() -> io::Result<ProgramState>) -> io::Result<()> {
    loop {
        // Start timer
        let start = time::SystemTime::now();

        // Execute function
        let result = func()?;

        // Handle execution result
        match result {
            ProgramState::Exiting => return Ok(()),
            ProgramState::Running => {
                // Rate limit loop iteration
                let elapsed = start.elapsed().unwrap().as_millis();

                if elapsed < TICK_DURATION {
                    let delta = TICK_DURATION - elapsed;
                    let duration = time::Duration::from_millis(delta as u64);
                    thread::sleep(duration);
                }
            }
        };
    }
}
