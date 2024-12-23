use std::io;

use crossterm::event;
use ratatui::{self, text::Text, DefaultTerminal, Frame};

fn main() {
    let mut terminal = ratatui::init();

    let mut app = App::default();
    let _ = app.run(&mut terminal);

    ratatui::restore();
}

#[derive(Debug)]
struct App {
    exit: bool,
}

impl App {
    pub fn run(&mut self, terminal: &mut DefaultTerminal) -> io::Result<()> {
        terminal.clear()?;

        while !self.exit {
            terminal.draw(|frame| self.draw(frame))?;
            self.handle_events()?;
        }

        Ok(())
    }

    fn draw(&self, frame: &mut Frame) {
        frame.render_widget(Text::raw("Hello World!"), frame.area());
    }

    fn handle_events(&mut self) -> io::Result<()> {
        let event = event::read()?;

        match event {
            event::Event::Key(event) => {
                if event.code == event::KeyCode::Char('q') {
                    self.exit = true;
                }
            }
            _ => {}
        }

        Ok(())
    }
}

impl Default for App {
    fn default() -> Self {
        App { exit: false }
    }
}
