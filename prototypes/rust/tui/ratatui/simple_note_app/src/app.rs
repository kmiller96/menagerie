use std::io;
use std::thread;
use std::time;

use ratatui;

pub struct App;

impl App {
    pub fn new() -> Self {
        App
    }

    pub fn run(&self, terminal: &mut ratatui::DefaultTerminal) -> io::Result<()> {
        terminal.clear()?;

        terminal.draw(|frame| self.draw(frame))?;

        thread::sleep(time::Duration::from_secs(2));

        Ok(())
    }

    pub fn draw(&self, frame: &mut ratatui::Frame) {
        frame.render_widget("Hello World!", frame.area());
    }
}
