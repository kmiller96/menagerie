use std::io;
use std::thread;
use std::time;

use ratatui::style::Stylize;
use ratatui::{style, widgets, DefaultTerminal, Frame};

pub struct App;

impl App {
    pub fn new() -> Self {
        App
    }

    pub fn run(&self, terminal: &mut DefaultTerminal) -> io::Result<()> {
        terminal.clear()?;

        terminal.draw(|frame| self.draw(frame))?;

        thread::sleep(time::Duration::from_secs(2));

        Ok(())
    }

    pub fn draw(&self, frame: &mut Frame) {
        let list = widgets::List::new(vec!["Item 1", "Item 2", "Item 3"])
            .highlight_style(style::Style::new().italic())
            .highlight_symbol(">>");

        frame.render_widget(list, frame.area());
    }
}
