use std::io::{self, Write};

use anyhow::Result;
use crossterm::{cursor, event, queue, style};

#[derive(Debug, PartialEq)]
enum AppStatus {
    Running,
    Quit,
}

#[derive(Debug)]
pub struct App {
    status: AppStatus,
    stdout: io::Stdout,
}

impl App {
    /** Initializes the application */
    pub fn init() -> Self {
        App {
            status: AppStatus::Running,
            stdout: io::stdout(),
        }
    }

    /** Runs the application loop */
    pub fn run(&mut self) -> Result<()> {
        loop {
            self.draw()?;
            self.handle_events()?;

            if self.status == AppStatus::Quit {
                break;
            }
        }

        Ok(())
    }

    /** Renders the terminal graphics */
    fn draw(&mut self) -> io::Result<()> {
        queue!(self.stdout, cursor::MoveTo(1, 1), style::Print("Hello!"))?;
        self.stdout.flush()?;

        Ok(())
    }

    /** Handles the application events */
    fn handle_events(&mut self) -> Result<()> {
        let event = event::read()?;

        match event {
            // -- Handle key events -- //
            event::Event::Key(event) => {
                if is_quit_event(event) {
                    self.status = AppStatus::Quit;
                }
            }
            // -- Default Handler -- //
            _ => {}
        }

        Ok(())
    }
}

// TODO: Should I move this to a separate module?
/** Determines if the event is a quit event */
fn is_quit_event(event: event::KeyEvent) -> bool {
    event.kind == event::KeyEventKind::Press && event.code == event::KeyCode::Char('q')
}
