use crate::coordinate::Coordinate;

// ------------- //
// -- Structs -- //
// ------------- //

// /// Defines a single pipeline in the terminal.
pub struct Pipe {
    momentum: Coordinate,
    pub segments: Vec<Coordinate>,
}

impl Pipe {
    /// Creates a new, empty Pipe.
    pub fn new(start: Coordinate) -> Self {
        Pipe {
            momentum: match start {
                Coordinate { x: 0, y: 0 } => Coordinate { x: 1, y: 0 },
                Coordinate { x: 0, y: _ } => Coordinate { x: 1, y: 0 },
                Coordinate { x: _, y: 0 } => Coordinate { x: 0, y: 1 },
                _ => panic!("Pipes must start on the top or left edge of the map"),
            },
            segments: vec![start],
        }
    }

    /// Gets the start of the pipe.
    pub fn start(&self) -> Coordinate {
        self.segments[0]
    }

    /// Gets the end of the pipe.
    pub fn end(&self) -> Coordinate {
        *self
            .segments
            .last()
            .expect("Pipe always has at least one segment")
    }

    /// Randomly grows the pipe by one segment.
    ///
    /// NOTE: At the moment, this is all placeholder logic. It just grows in a
    /// straight line. But eventually it will grow in random directions.
    pub fn grow(&mut self) {
        let head = self.end();

        let segment = Coordinate {
            x: head.x + self.momentum.x,
            y: head.y + self.momentum.y,
        };

        self.segments.push(segment);
    }
}
