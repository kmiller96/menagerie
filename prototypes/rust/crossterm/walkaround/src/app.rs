use std::io::{self, Write};

use anyhow::Result;
use crossterm::{cursor, event, queue, style, terminal};

#[derive(Debug)]
struct Player {
    position: (u16, u16), // (x, y)
}

#[derive(Debug, PartialEq)]
enum AppStatus {
    Running,
    Quit,
}

#[derive(Debug)]
pub struct App {
    status: AppStatus,
    stdout: io::Stdout,
    player: Player,
}

impl App {
    /** Initializes the application */
    pub fn init() -> Self {
        App {
            status: AppStatus::Running,
            stdout: io::stdout(),
            player: Player { position: (0, 0) },
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
        let (width, height) = terminal::size()?;

        // Draw map background
        for y in 0..height {
            for x in 0..width {
                queue!(self.stdout, cursor::MoveTo(x, y), style::Print("."))?;
            }
        }

        // Draw character
        queue!(
            self.stdout,
            cursor::MoveTo(self.player.position.0, self.player.position.1),
            style::Print("O"),
        )?;

        // Draw debug info
        let width_debug = format!("Width: {}", width);
        let height_debug = format!("Height: {}", height);

        queue!(
            self.stdout,
            cursor::MoveTo(width - width_debug.len() as u16, height - 2),
            style::Print(width_debug),
            cursor::MoveTo(width - height_debug.len() as u16, height - 1),
            style::Print(height_debug),
        )?;

        // Flush & Return
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
    let q_press =
        event.kind == event::KeyEventKind::Press && event.code == event::KeyCode::Char('q');

    let esc_press = event.kind == event::KeyEventKind::Press && event.code == event::KeyCode::Esc;

    let ctrl_c = event.kind == event::KeyEventKind::Press
        && event.code == event::KeyCode::Char('c')
        && event.modifiers == event::KeyModifiers::CONTROL;

    q_press || esc_press || ctrl_c
}
