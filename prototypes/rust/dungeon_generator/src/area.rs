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
    dimensions: Dimensions,
    tiles: Vec<Vec<Tile>>,
}

impl Area {
    /// Creates a new area with given dimensions.
    pub fn new(dimensions: Dimensions) -> Self {
        let (width, height) = dimensions;
        let mut tiles = Vec::new();

        for _ in 0..width {
            let mut column = Vec::new();

            for _ in 0..height {
                column.push(Tile::Empty);
            }

            tiles.push(column);
        }

        Area {
            dimensions: (width, height),
            tiles,
        }
    }

    /// Blits another area onto this one at the given top-left coordinate.
    pub fn blit(&mut self, other: &Area, position: Coordinate) {
        let (px, py) = position;

        for x in 0..other.width() {
            for y in 0..other.height() {
                self[(px + x, py + y)] = other[(x, y)].clone();
            }
        }
    }

    /// Returns the height (y) of the area.
    #[allow(dead_code)]
    pub fn height(&self) -> u32 {
        self.dimensions.1
    }

    /// Returns the width (x) of the area.
    #[allow(dead_code)]
    pub fn width(&self) -> u32 {
        self.dimensions.0
    }

    pub fn dimensions(&self) -> Dimensions {
        self.dimensions
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
