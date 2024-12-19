use std::io;

mod structs;
use structs::LoopClock;

use crossterm::event::{self, KeyCode, KeyEventKind};

use ratatui::{
    style::Color,
    widgets::canvas::{Canvas, Points},
    DefaultTerminal,
};

// fn run(mut terminal: DefaultTerminal) -> io::Result<()> {
//     loop {
//         terminal.draw(|frame| {
//             let greeting = Paragraph::new("Hello Ratatui! (press 'q' to quit)")
//                 .white()
//                 .on_blue();
//             frame.render_widget(greeting, frame.area());
//         })?;

//         if let event::Event::Key(key) = event::read()? {
//             if key.kind == KeyEventKind::Press && key.code == KeyCode::Char('q') {
//                 return Ok(());
//             }
//         }
//     }
// }

enum Event {
    Quit,
    Paint(usize, usize, char),
}

// Information about the current tick.
struct App {
    clock: LoopClock,
    canvas: [Option<char>; 50 * 50], // Canvas is a 50x50 grid
}

impl App {
    fn new() -> App {
        App {
            clock: LoopClock::new(),
            canvas: [None; 50 * 50],
        }
    }

    // Paint a character on the canvas at a specific position
    fn paint(&mut self, x: usize, y: usize, c: char) {
        self.canvas[y * 50 + x] = Some(c);
    }

    // Renders the UI to the screen
    fn draw(&self, terminal: &mut DefaultTerminal) {
        let _ = terminal.draw(|frame| {
            frame.render_widget(
                Canvas::default().paint(|ctx| {
                    ctx.draw(&Points {
                        coords: &[(0.0, 0.0), (1.0, 1.0)],
                        color: Color::Red,
                    })
                }),
                frame.area(),
            )
        });
    }

    // Handle events
    fn handle(&self, terminal: &DefaultTerminal) -> Option<Event> {
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
            match self.handle(terminal) {
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
