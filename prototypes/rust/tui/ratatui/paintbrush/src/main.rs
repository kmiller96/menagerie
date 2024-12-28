use std::io;

mod structs;
use structs::LoopClock;

use crossterm::event::{self, KeyCode, KeyEventKind};

use ratatui::{
    style::Color,
    text::Text,
    widgets::canvas::{Canvas, Points},
    DefaultTerminal,
};

const ROWS: usize = 10;
const COLS: usize = 50;

const ALPHABET: &str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

enum Event {
    Quit,
    Paint(usize, usize, char),
}

// Information about the current tick.
struct App {
    clock: LoopClock,
    canvas: [Option<char>; ROWS * COLS],
}

impl App {
    fn new() -> App {
        App {
            clock: LoopClock::new(),
            canvas: [None; ROWS * COLS],
        }
    }

    // Paint a character on the canvas at a specific position
    fn paint(&mut self, x: usize, y: usize, c: char) {
        todo!();
    }

    // Renders the UI to the screen
    fn draw(&self, terminal: &mut DefaultTerminal) {
        // -- Build content -- //
        let mut content = String::new();

        for i in 0..(ROWS * COLS) {
            let c = match self.canvas[i] {
                Some(c) => c,
                // None => ' ',
                None => ALPHABET.chars().nth(i % ALPHABET.len()).unwrap(),
            };

            content.push(c);

            if (i + 1) % COLS == 0 {
                content.push('\n');
            }
        }

        // -- Draw content -- //
        let _ = terminal.draw(|frame| frame.render_widget(Text::raw(content), frame.area()));
    }

    // Handle events
    fn handle(&self) -> Option<Event> {
        let keyevent = match event::read() {
            Ok(event) => event,
            Err(_) => return None,
        };

        if let event::Event::Key(key) = keyevent {
            if key.kind == KeyEventKind::Press && key.code == KeyCode::Char('q') {
                return Some(Event::Quit);
            }
        }

        None
    }

    // Runs the TUI
    fn run(&mut self, terminal: &mut DefaultTerminal) {
        loop {
            // Run event loop
            self.draw(terminal);
            match self.handle() {
                Some(Event::Quit) => break,
                _ => (),
            }

            // FPS limiter
            self.clock.throttle();
            self.clock.tick();
        }
    }
}

fn main() -> io::Result<()> {
    // Setup terminal
    let mut terminal = ratatui::init();
    terminal.clear()?;

    // Run the app
    let mut app = App::new();
    app.run(&mut terminal);

    // Restore terminal
    ratatui::restore();
    Ok(())
}
