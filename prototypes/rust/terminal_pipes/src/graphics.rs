//! Defines the graphics module, which handles rendering to the terminal.

use std::io::{stdout, Write};

use crossterm::{cursor, queue, style::Print};

pub struct Graphics {
    pub stdout: std::io::Stdout,
}

impl Graphics {
    // ------------------- //
    // -- Class Methods -- //
    // ------------------- //

    pub fn new() -> Self {
        Graphics { stdout: stdout() }
    }

    // ---------------------- //
    // -- Instance Methods -- //
    // ---------------------- //

    /// Flushes the queued commands to the terminal.
    pub fn flush(&mut self) -> std::io::Result<()> {
        self.stdout.flush()?;
        Ok(())
    }

    /// Clears the terminal screen.
    pub fn clear(&mut self) -> std::io::Result<&mut Self> {
        crossterm::execute!(
            self.stdout,
            crossterm::terminal::Clear(crossterm::terminal::ClearType::All)
        )?;

        Ok(self)
    }

    /// Prints text to the terminal.
    pub fn print(&mut self, x: u16, y: u16, text: &str) -> std::io::Result<&mut Self> {
        queue!(self.stdout, cursor::MoveTo(x, y), Print(text))?;
        Ok(self)
    }

    /// Queues a generic command to be executed later.
    pub fn queue(&mut self, command: impl crossterm::Command) -> std::io::Result<&mut Self> {
        queue!(self.stdout, command)?;
        Ok(self)
    }
}
