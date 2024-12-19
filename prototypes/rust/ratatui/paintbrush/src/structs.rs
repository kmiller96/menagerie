use std::time::Instant;

const FPS: u32 = 60;
const TICK_DURATION: u32 = 1000 / FPS;

// ------------------- //
// -- Loop Metadata -- //
// ------------------- //

pub struct LoopClock {
    start: Instant,
}

impl LoopClock {
    // Creates a new LoopClock instance.
    pub fn new() -> LoopClock {
        LoopClock {
            start: Instant::now(),
        }
    }

    // "Ticks" the clock to the next frame.
    pub fn tick(&mut self) {
        self.start = Instant::now();
    }

    // Returns the time elapsed since the last tick.
    pub fn elapsed(&self) -> u128 {
        self.start.elapsed().as_millis()
    }

    // Waits until the next frame is ready to draw.
    pub fn throttle(&self) {
        let remaining = TICK_DURATION as i32 - (self.elapsed() as i32);

        if remaining > 0 {
            std::thread::sleep(std::time::Duration::from_millis(remaining as u64));
        }
    }
}
