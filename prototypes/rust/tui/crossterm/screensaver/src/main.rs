use std::{
    io::{self, Write},
    time,
};

use crossterm::{
    cursor,
    event::{self, Event, KeyCode},
    execute, queue, style, terminal,
};
use rand::Rng;

const FPS: u128 = 32;
const TICK_DURATION: u128 = 1000 / FPS;
const EVENT_TIMEOUT_MS: u64 = 50;

const SCREEN_WIDTH: usize = 80;
const SCREEN_HEIGHT: usize = 24;

const N_BALLS: u8 = 10;

// TODO: Optimise the terminal draw by managing a virtual "screen" and only
// rendering what changes.

// ---------- //
// -- Ball -- //
// ---------- //

struct Ball {
    pub position: (usize, usize),
    pub velocity: (isize, isize),
}

impl Ball {
    /// Creates a new ball.
    pub fn new(position: (usize, usize), velocity: (isize, isize)) -> Self {
        Self { position, velocity }
    }

    /// Updates the ball's position based on its velocity.
    pub fn tick(&mut self) {
        let x0 = self.position.0;
        let y0 = self.position.1;

        let vx = self.velocity.0;
        let vy = self.velocity.1;

        self.position = (x0.saturating_add_signed(vx), y0.saturating_add_signed(vy));
    }
}

// ----------------- //
// -- Application -- //
// ----------------- //

enum AppStatus {
    Running,
    Exiting,
}

enum AppEvent {
    Quit,
    // Other events can be added here
}

struct Application {
    status: AppStatus,
    events: Vec<AppEvent>, // TODO: Replace with VecDeque for efficiency. Also maybe make it not possible to duplicate events?
    stdout: io::Stdout,
    balls: Vec<Ball>,
}

impl Drop for Application {
    fn drop(&mut self) {
        terminal::disable_raw_mode().expect("Failed to disable raw mode");
        execute!(
            self.stdout,
            terminal::Clear(terminal::ClearType::All),
            cursor::Show,
            style::ResetColor,
            terminal::LeaveAlternateScreen,
        )
        .expect("Failed to restore terminal");
    }
}

impl Application {
    pub fn init() -> Self {
        // Initialise the stdout
        let mut stdout = io::stdout();

        terminal::enable_raw_mode().expect("Failed to enable raw mode");
        execute!(
            stdout,
            terminal::EnterAlternateScreen,
            cursor::Hide,
            style::SetForegroundColor(style::Color::Green)
        )
        .expect("Failed to initialise terminal");

        // Setup the balls with a random position and velocity
        let mut balls = vec![];
        let mut rng = rand::rng();

        for _ in 0..N_BALLS {
            let ball = Ball::new(
                (
                    rng.random_range(1..SCREEN_WIDTH - 1),
                    rng.random_range(1..SCREEN_HEIGHT - 1),
                ),
                (
                    if rng.random_bool(0.5) { 1 } else { -1 },
                    if rng.random_bool(0.5) { 1 } else { -1 },
                ),
            );

            balls.push(ball);
        }

        // Return the program state
        Self {
            status: AppStatus::Running,
            events: Vec::new(),
            stdout,
            balls,
        }
    }

    /// Runs the main application event loop.
    ///
    /// This event loop rate limits the application draw to the configured FPS
    /// while still allowing user input between redraws.
    pub fn run(&mut self) -> Result<(), io::Error> {
        loop {
            // Start loop timer
            let start = time::SystemTime::now();

            // Run main event loop
            self.handle();
            self.update();
            self.draw()?;

            // Special check to break from event loop
            match self.status {
                AppStatus::Exiting => return Ok(()),
                _ => { /* Continue running */ }
            }

            // Capture user input until tick duration reached.
            while start.elapsed().unwrap().as_millis() < TICK_DURATION {
                self.capture_user_input()?;
            }
        }
    }

    /// Captures crossterm events
    fn capture_user_input(&mut self) -> io::Result<()> {
        // Determine if there is an event to read.
        let result = event::poll(time::Duration::from_millis(EVENT_TIMEOUT_MS))?;

        // Process result if there is an event waiting.
        if result {
            let e = event::read()?;
            match e {
                Event::Key(event) => {
                    match event.code {
                        KeyCode::Char('q') | KeyCode::Esc => {
                            self.events.push(AppEvent::Quit);
                        }
                        _ => { /* Ignore all other inputs */ }
                    }
                }
                _ => { /* We can ignore all events we don't explicitly handle. */ }
            }
        }

        // Return ok
        Ok(())
    }

    /// Processes user input and application state into program events.
    fn handle(&mut self) {
        const LHS_BOUND: usize = 1;
        const RHS_BOUND: usize = SCREEN_WIDTH - 2;
        const TOP_BOUND: usize = 1;
        const BOTTOM_BOUND: usize = SCREEN_HEIGHT - 2;

        // Determine what the ball should be doing
        for ball in &mut self.balls {
            // Bounce off walls
            if ball.position.0 <= LHS_BOUND {
                ball.velocity.0 = ball.velocity.0.abs();
            }
            if ball.position.0 >= RHS_BOUND {
                ball.velocity.0 = -ball.velocity.0.abs();
            }
            if ball.position.1 <= TOP_BOUND {
                ball.velocity.1 = ball.velocity.1.abs();
            }
            if ball.position.1 >= BOTTOM_BOUND {
                ball.velocity.1 = -ball.velocity.1.abs();
            }
        }
    }

    /// Updates the program state based on events.
    fn update(&mut self) {
        // Tick the balls
        for ball in &mut self.balls {
            ball.tick();
        }

        // Handle User Input
        while self.events.len() > 0 {
            let event = self.events.remove(0);

            match event {
                AppEvent::Quit => {
                    self.status = AppStatus::Exiting;
                }
            }
        }
    }

    /// Draws the current program state to the terminal.
    fn draw(&mut self) -> io::Result<()> {
        // Clear terminal to clean state
        queue!(self.stdout, terminal::Clear(terminal::ClearType::All))?;

        // Add border
        for y in 0..SCREEN_HEIGHT {
            for x in 0..SCREEN_WIDTH {
                let char =
                    if (x == 0 || x == SCREEN_WIDTH - 1) && (y == 0 || y == SCREEN_HEIGHT - 1) {
                        "+"
                    } else if y == 0 || y == SCREEN_HEIGHT - 1 {
                        "-"
                    } else if x == 0 || x == SCREEN_WIDTH - 1 {
                        "|"
                    } else {
                        continue;
                    };

                queue!(
                    self.stdout,
                    cursor::MoveTo(x as u16, y as u16),
                    style::Print(char)
                )?;
            }
        }

        // Draw the balls
        for ball in &self.balls {
            queue!(
                self.stdout,
                cursor::MoveTo(ball.position.0 as u16, ball.position.1 as u16),
                style::Print("O"),
            )?;
        }

        // Flush all queued commands
        self.stdout.flush()?;

        // Draw successful
        Ok(())
    }
}

// ------------------ //
// -- Main Routine -- //
// ------------------ //

fn main() -> io::Result<()> {
    let mut app = Application::init();

    app.run()?;

    Ok(())
}
