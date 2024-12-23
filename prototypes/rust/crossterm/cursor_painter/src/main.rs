use std::io::{self, Write};

use crossterm::{
    cursor, event, execute, queue,
    style::{self, Stylize},
    terminal::{
        self, disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen,
    },
};

fn main() -> io::Result<()> {
    let mut stdout = io::stdout();
    let mut app = App::init();

    execute!(stdout, EnterAlternateScreen)?;
    enable_raw_mode()?;

    app.run(&mut stdout)?;

    disable_raw_mode()?;
    execute!(stdout, LeaveAlternateScreen)?;
    Ok(())

    // for y in 0..40 {
    //     for x in 0..150 {
    //         if (y == 0 || y == 40 - 1) || (x == 0 || x == 150 - 1) {
    //             // in this loop we are more efficient by not flushing the buffer.
    //             stdout
    //                 .queue(cursor::MoveTo(x, y))?
    //                 .queue(style::PrintStyledContent("█".magenta()))?;
    //         }
    //     }
    // }
}

#[derive(Debug)]
struct App {
    exit: bool,
}

impl App {
    pub fn init() -> Self {
        App { exit: false }
    }

    pub fn run(&mut self, stdout: &mut io::Stdout) -> io::Result<()> {
        execute!(stdout, terminal::Clear(terminal::ClearType::All))?;

        while !self.exit {
            self.draw(stdout)?;
            self.handle_events()?;
        }

        stdout.flush()?;
        Ok(())
    }

    fn draw(&self, stdout: &mut io::Stdout) -> io::Result<()> {
        queue!(stdout, cursor::MoveTo(1, 1), style::Print("Hello World!"))?;

        stdout.flush()?;

        Ok(())
    }

    fn handle_events(&mut self) -> io::Result<()> {
        let event = event::read()?;

        match event {
            event::Event::Key(e) => {
                if e.kind == event::KeyEventKind::Press {
                    self.handle_keypress(e)?;
                }
            }
            _ => {}
        }

        Ok(())
    }

    fn handle_keypress(&mut self, key: event::KeyEvent) -> io::Result<()> {
        match key.code {
            event::KeyCode::Char('q') => {
                self.exit = true;
            }
            _ => {}
        }

        Ok(())
    }
}
