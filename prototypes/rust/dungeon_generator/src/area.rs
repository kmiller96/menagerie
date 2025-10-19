use std::fmt::{self, Display, Formatter};
use std::ops::{Index, IndexMut};

use crate::tile::Tile;
use crate::utils::Coordinate;
use crate::utils::Dimensions;

//
// TODO: Flesh this idea out and, evenetually, replace the Map struct with it.
//

/// Represents an area which is made up of tiles.
#[derive(Debug)]
pub struct Area {
    tiles: Vec<Vec<Tile>>,
}

impl Area {
    /// Returns the height (y) of the area.
    pub fn height(&self) -> u32 {
        self.tiles.len() as u32
    }

    /// Returns the width (x) of the area.
    pub fn width(&self) -> u32 {
        if self.tiles.is_empty() {
            0
        } else {
            self.tiles[0].len() as u32
            // TODO: Should we verify that all rows are the same length?
        }
    }

    pub fn dimensions(&self) -> Dimensions {
        todo!("Implement dimensions method")
    }
}

// ------------------ //
// -- Area Display -- //
// ------------------ //

impl Display for Area {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        for y in 0..self.dimensions().1 {
            for x in 0..self.dimensions().0 {
                write!(f, "{}", self.tiles[x as usize][y as usize])?;
            }
            writeln!(f)?;
        }
        Ok(())
    }
}

// ------------------- //
// -- Area Indexing -- //
// ------------------- //

impl Index<Coordinate> for Area {
    type Output = Tile;

    fn index(&self, index: Coordinate) -> &Self::Output {
        &self.tiles[index.0 as usize][index.1 as usize]
    }
}

impl IndexMut<Coordinate> for Area {
    fn index_mut(&mut self, index: Coordinate) -> &mut Self::Output {
        &mut self.tiles[index.0 as usize][index.1 as usize]
    }
}

// -------------------- //
// -- Area Iteration -- //
// -------------------- //

// TODO
