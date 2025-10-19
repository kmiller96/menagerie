use std::fmt::{self, Display, Formatter};
use std::ops::{Index, IndexMut};

use crate::tile::Tile;
use crate::utils::{Coordinate, Dimensions};

const HORIZONTAL_BORDER_STRING: char = '-';
const VERTICAL_BORDER_CHAR: char = '|';
const CORNER_BORDER_CHAR: char = '+';

// ---------------- //
// -- Map Object -- //
// ---------------- //

/// Represents the final map.
#[derive(Debug)]
pub struct Map {
    dimensions: Dimensions,
    tiles: Vec<Vec<Tile>>,
}

impl Map {
    /// Initializes a new map with given dimensions.
    pub fn new(width: u32, height: u32) -> Self {
        let mut tiles = Vec::new();

        for _ in 0..width {
            let mut column = Vec::new();

            for _ in 0..height {
                column.push(Tile::Empty);
            }

            tiles.push(column);
        }

        Map {
            dimensions: (width, height),
            tiles,
        }
    }
}

// ---------------------------- //
// -- Display Implementation -- //
// ---------------------------- //

impl Display for Map {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        // Load in the border characters
        let hb = HORIZONTAL_BORDER_STRING.to_string();
        let vb = VERTICAL_BORDER_CHAR.to_string();
        let cb = CORNER_BORDER_CHAR.to_string();

        // Determine the horizontal border dimensions
        let horzontal_border =
            cb.clone() + &hb.repeat(self.dimensions.0 as usize).clone() + &cb.clone();

        // Print the top border
        writeln!(f, "{}", horzontal_border)?;

        // Print the map rows
        for y in 0..self.dimensions.1 {
            write!(f, "{}", &vb)?;

            for x in 0..self.dimensions.0 {
                write!(f, "{}", self.tiles[x as usize][y as usize])?;
            }

            write!(f, "{}\n", vb)?;
        }

        // Print the bottom border
        writeln!(f, "{}", horzontal_border)?;

        // Indicate successful formatting
        Ok(())
    }
}

// ------------------ //
// -- Map Indexing -- //
// ------------------ //

impl Index<Coordinate> for Map {
    type Output = Tile;

    fn index(&self, index: Coordinate) -> &Self::Output {
        &self.tiles[index.0 as usize][index.1 as usize]
    }
}

impl IndexMut<Coordinate> for Map {
    fn index_mut(&mut self, index: Coordinate) -> &mut Self::Output {
        &mut self.tiles[index.0 as usize][index.1 as usize]
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
