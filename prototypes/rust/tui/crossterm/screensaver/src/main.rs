use std::{
    io::{self, Write},
    time,
};

use crossterm::{
    cursor,
    event::{self, Event, KeyCode},
    execute, queue, style, terminal,
};

const FPS: u128 = 5;
const TICK_DURATION: u128 = 1000 / FPS;
const EVENT_TIMEOUT_MS: u64 = 50;

// ----------- //
// -- Enums -- //
// ----------- //

enum ProgramStatus {
    Running,
    Exiting,
}

enum AppEvent {
    Quit,
    // Other events can be added here
}

// ----------------- //
// -- Application -- //
// ----------------- //

struct Application {
    status: ProgramStatus,
    events: Vec<AppEvent>, // TODO: Replace with VecDeque for efficiency
    stdout: io::Stdout,
    counter: u32, // TEMP FOR TESTING ONLY
}

impl Drop for Application {
    fn drop(&mut self) {
        terminal::disable_raw_mode().expect("Failed to disable raw mode");
        execute!(
            self.stdout,
            terminal::LeaveAlternateScreen,
            style::ResetColor
        )
        .expect("Failed to restore terminal");
    }
}

impl Application {
    pub fn init() -> Self {
        // Initialise the stdout
        let mut stdout = io::stdout();

        terminal::enable_raw_mode().expect("Failed to enable raw mode");
        execute!(
            stdout,
            terminal::EnterAlternateScreen,
            style::SetForegroundColor(style::Color::Green)
        )
        .expect("Failed to initialise terminal");

        // Return the program state
        Self {
            status: ProgramStatus::Running,
            events: Vec::new(),
            stdout,
            counter: 0, // TEMP FOR TESTING ONLY
        }
    }

    /// Runs the main application event loop.
    ///
    /// This event loop rate limits the application draw to the configured FPS
    /// while still allowing user input between redraws.
    pub fn run(&mut self) -> Result<(), io::Error> {
        loop {
            // Start loop timer
            let start = time::SystemTime::now();

            // Run main event loop
            self.handle();
            self.update();
            self.draw()?;

            // Capture user input until tick duration reached.
            while start.elapsed().unwrap().as_millis() < TICK_DURATION {
                self.capture_events()?;
            }
        }
    }

    /// Captures crossterm events
    fn capture_events(&mut self) -> io::Result<()> {
        // Determine if there is an event to read.
        let result = event::poll(time::Duration::from_millis(EVENT_TIMEOUT_MS))?;

        // Process result if there is an event waiting.
        if result {
            let e = event::read()?;
            match e {
                Event::Key(event) => {
                    match event.code {
                        KeyCode::Char('q') | KeyCode::Esc => {
                            self.events.push(AppEvent::Quit);
                        }
                        _ => { /* Ignore all other inputs */ }
                    }
                }
                _ => { /* We can ignore all events we don't explicitly handle. */ }
            }
        }

        // Return ok
        Ok(())
    }

    /// Processes user input and application state into program events.
    fn handle(&mut self) {
        if self.counter >= 100 {
            self.status = ProgramStatus::Exiting;
        }
    }

    /// Updates the program state based on events.
    fn update(&mut self) {
        while self.events.len() > 0 {
            let event = self.events.remove(0);

            match event {
                AppEvent::Quit => {
                    std::process::exit(0);
                } // Handle other events here
            }
        }

        self.counter += 1; // TEMP FOR TESTING ONLY
    }

    /// Draws the current program state to the terminal.
    fn draw(&mut self) -> io::Result<()> {
        // Queue up drawing commands
        queue!(
            self.stdout,
            terminal::Clear(terminal::ClearType::All),
            cursor::MoveTo(0, 0),
            style::Print(format!("Counter: {}\n", self.counter))
        )?;

        // Flush all queued commands
        self.stdout.flush()?;

        // Draw successful
        Ok(())
    }
}

// ------------------ //
// -- Main Routine -- //
// ------------------ //

fn main() -> io::Result<()> {
    let mut app = Application::init();

    app.run()?;

    Ok(())
}
