use std::fmt::{self, Display, Formatter};
use std::ops::{Index, IndexMut};

use crate::area::Area;
use crate::tile::Tile;
use crate::utils::Coordinate;

const HORIZONTAL_BORDER_STRING: char = '-';
const VERTICAL_BORDER_CHAR: char = '|';
const CORNER_BORDER_CHAR: char = '+';

// TODO: Simplify. Isn't a map basically just an area with borders?

// ---------------- //
// -- Map Object -- //
// ---------------- //

/// Represents the final map.
#[derive(Debug)]
pub struct Map {
    area: Area,
}

impl Map {
    /// Initializes a new map with given dimensions.
    pub fn new(area: Area) -> Self {
        Map { area }
    }
}

// ---------------------------- //
// -- Display Implementation -- //
// ---------------------------- //

impl Display for Map {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        // Get dimensions
        let (width, height) = self.area.dimensions();

        // Top border
        write!(f, "{}", CORNER_BORDER_CHAR)?;
        for _ in 0..width {
            write!(f, "{}", HORIZONTAL_BORDER_STRING)?;
        }
        writeln!(f, "{}", CORNER_BORDER_CHAR)?;

        // Map rows
        for y in 0..height {
            write!(f, "{}", VERTICAL_BORDER_CHAR)?;
            for x in 0..width {
                write!(f, "{}", self.area[(x, y)])?;
            }
            writeln!(f, "{}", VERTICAL_BORDER_CHAR)?;
        }

        // Bottom border
        // TODO: Refactor to avoid code duplication with top border
        write!(f, "{}", CORNER_BORDER_CHAR)?;
        for _ in 0..width {
            write!(f, "{}", HORIZONTAL_BORDER_STRING)?;
        }
        writeln!(f, "{}", CORNER_BORDER_CHAR)?;

        // Success
        Ok(())
    }
}

// ------------------ //
// -- Map Indexing -- //
// ------------------ //

impl Index<Coordinate> for Map {
    type Output = Tile;

    fn index(&self, index: Coordinate) -> &Self::Output {
        &self.area[index]
    }
}

impl IndexMut<Coordinate> for Map {
    fn index_mut(&mut self, index: Coordinate) -> &mut Self::Output {
        &mut self.area[index]
    }
}

// ------------------- //
// -- Map Iteration -- //
// ------------------- //

// HELPME: I think the right way to do this is to implement IntoIterator for the
// map, but I'm not sure how to do that without it looking like a shitshow.
//
// ...
//
