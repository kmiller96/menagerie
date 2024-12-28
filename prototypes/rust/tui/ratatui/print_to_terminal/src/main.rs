use std::io;

use crossterm::event::{self, Event, KeyCode, KeyEvent, KeyEventKind};
use ratatui::{layout::Rect, text::Span, DefaultTerminal, Frame};

#[derive(Debug, Default)]
struct App {
    exit: bool,
}

impl App {
    pub fn run(&mut self, terminal: &mut DefaultTerminal) -> io::Result<()> {
        while !self.exit {
            terminal.draw(|frame| self.draw(frame))?;
            self.handle_events()?;
        }
        Ok(())
    }

    fn draw(&self, frame: &mut Frame) {
        frame.render_widget(Span::raw("Hello world!"), frame.area());

        self.print(frame, "?", 5, 5);
        self.print(frame, "?", 5, 6);
        self.print(frame, "?", 6, 5);
    }

    fn print(&self, frame: &mut Frame, char: &str, x: u16, y: u16) {
        frame.render_widget(Span::raw(char), Rect::new(x, y, 1, 1));
    }

    fn handle_events(&mut self) -> io::Result<()> {
        let event = event::read()?;

        match event {
            Event::Key(KeyEvent {
                code: KeyCode::Char('q'),
                kind: KeyEventKind::Press,
                ..
            }) => {
                self.exit = true;
            }
            _ => {}
        }

        Ok(())
    }
}

fn main() -> io::Result<()> {
    let mut terminal = ratatui::init();

    let mut app = App::default();
    let _ = app.run(&mut terminal);

    ratatui::restore();
    Ok(())
}
