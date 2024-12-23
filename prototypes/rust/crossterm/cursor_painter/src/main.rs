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

    app.run()?;

    disable_raw_mode()?;
    execute!(stdout, LeaveAlternateScreen)?;

    Ok(())
}

#[derive(Debug)]
struct App {
    exit: bool,
    stdout: io::Stdout,
}

impl App {
    /** Creates a new instance of the app. */
    pub fn init() -> Self {
        let mut stdout = io::stdout();

        App {
            exit: false,
            stdout,
        }
    }

    /** Runs the app. */
    pub fn run(&mut self) -> io::Result<()> {
        self.setup()?;

        while !self.exit {
            self.draw()?;
            self.handle_events()?;
        }

        self.stdout.flush()?;
        Ok(())
    }

    /** Performs the initial draw. */
    fn setup(&mut self) -> io::Result<()> {
        queue!(
            self.stdout,
            terminal::Clear(terminal::ClearType::All),
            cursor::MoveTo(1, 1),
            style::Print("Hello World!"),
            cursor::MoveTo(0, 0)
        )?;

        self.stdout.flush()?;
        Ok(())
    }

    /** Draws the terminal screen. */
    fn draw(&mut self) -> io::Result<()> {
        self.stdout.flush()?;

        Ok(())
    }

    /** Handles terminal events. */
    fn handle_events(&mut self) -> io::Result<()> {
        let event = event::read()?;

        match event {
            event::Event::Key(e) => match e.kind {
                event::KeyEventKind::Press => {
                    self.handle_keypress(e)?;
                }
                _ => {}
            },
            _ => {}
        }

        Ok(())
    }

    /** Handles keypress events. */
    fn handle_keypress(&mut self, key: event::KeyEvent) -> io::Result<()> {
        match key.code {
            // Exit the app
            event::KeyCode::Char('q') => {
                self.exit = true;
            }

            // Move the cursor
            event::KeyCode::Up | event::KeyCode::Char('w') => {
                queue!(self.stdout, cursor::MoveUp(1))?;
            }
            event::KeyCode::Down | event::KeyCode::Char('s') => {
                queue!(self.stdout, cursor::MoveDown(1))?;
            }
            event::KeyCode::Left | event::KeyCode::Char('a') => {
                queue!(self.stdout, cursor::MoveLeft(1))?;
            }
            event::KeyCode::Right | event::KeyCode::Char('d') => {
                queue!(self.stdout, cursor::MoveRight(1))?;
            }

            // Paint
            event::KeyCode::Char(' ') => {
                queue!(
                    self.stdout,
                    style::PrintStyledContent("█".bold()),
                    cursor::MoveLeft(1) // HACK: Move the cursor back to the left
                )?;
            }

            // Do nothing for other keys
            _ => {}
        }

        Ok(())
    }
}
