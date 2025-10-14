use rand::prelude::*;

/// Defines a single pipeline in the terminal.
pub struct Pipe {
    pub segments: Vec<(u16, u16)>,
    pub head: (u16, u16),
}

impl Pipe {
    /// Creates a new, empty Pipe.
    pub fn new() -> Self {
        let head = (3, 3); // TODO: Randomize starting position

        let mut segments = Vec::new();
        segments.push(head);

        Pipe { segments, head }
    }

    /// Grows the pipe by randomly adding a new segment.
    pub fn grow(&mut self) {
        let dx: i16;
        let dy: i16;

        if self.segments.len() == 1 {
            // First segment is always normal to wall
            // TODO: Figure out how to do this based on wall
            dx = 0;
            dy = 1;
        } else {
            let mut rng = rand::rng();

            dx = if rng.random::<bool>() { 1 } else { -1 };
            dy = if rng.random::<bool>() { 1 } else { -1 };
        }

        let segment = (
            (self.head.0 as i16 + dx) as u16,
            (self.head.1 as i16 + dy) as u16,
        );

        self.segments.push(segment);
        self.head = segment;
    }
}
