//! Defines a room within the dungeon.
//!
//! This is basically an Area but with predefined tiles.

use std::fmt::Display;

use crate::area::Area;
use crate::tile::Tile;
use crate::utils::Dimensions;

// ----------------- //
// -- Room Object -- //
// ----------------- //

pub struct Room {
    area: Area,
}

impl Room {
    /// Creates a new room with given dimensions.
    pub fn new(dimensions: Dimensions) -> Self {
        // Unpack dimensions
        let (inner_width, inner_height) = dimensions;

        let width = inner_width + 2;
        let height = inner_height + 2;

        // Create the area
        let mut area = Area::new((width, height));

        // Fill in walls around the edges
        for x in 0..width {
            area[(x, 0)] = Tile::Wall;
            area[(x, height - 1)] = Tile::Wall;
        }

        for y in 0..height {
            area[(0, y)] = Tile::Wall;
            area[(width - 1, y)] = Tile::Wall;
        }

        // Fill in floors in the interior
        for x in 1..(width - 1) {
            for y in 1..(height - 1) {
                area[(x, y)] = Tile::Floor;
            }
        }

        // Return the room
        Self { area }
    }

    pub fn area(&self) -> &Area {
        &self.area
    }
}

// ------------------ //
// -- Room Display -- //
// ------------------ //

impl Display for Room {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.area)
    }
}
