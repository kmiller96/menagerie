use rand::prelude::*;

use crate::coordinate::Coordinate;

pub struct Map {
    width: u16,
    height: u16,
}

impl Map {
    pub fn new(width: u16, height: u16) -> Self {
        Map { width, height }
    }

    pub fn contains(&self, coord: &Coordinate) -> bool {
        coord.x < self.width && coord.y < self.height
    }

    /// Generates a random coordinate on the map bounds.
    ///
    /// The coordinate will always be on the top or left edge of the map.
    pub fn random_start_coordinate(&self) -> Coordinate {
        let mut rng = rand::rng();

        match rng.random_range(0..2) {
            0 => Coordinate {
                x: rng.random_range(0..self.width),
                y: 0,
            },
            1 => Coordinate {
                x: 0,
                y: rng.random_range(0..self.height),
            },
            _ => unreachable!(),
        }
    }
}
