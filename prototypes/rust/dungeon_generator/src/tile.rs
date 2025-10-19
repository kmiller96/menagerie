use std::fmt::{self, Display, Formatter};

// --------------- //
// -- Tile Type -- //
// --------------- //

#[derive(Debug)]
pub enum TileType {
    Empty,
    Wall,
    Floor,
}

impl Display for TileType {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "{}",
            match self {
                TileType::Empty => " ",
                TileType::Wall => "#",
                TileType::Floor => ".",
            }
        )
    }
}

// ---------- //
// -- Tile -- //
// ---------- //

/// Represents a single tile in the map.
#[derive(Debug)]
pub struct Tile {
    pub value: TileType,
}

impl Display for Tile {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.value)
    }
}
