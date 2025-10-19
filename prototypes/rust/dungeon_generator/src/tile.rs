use std::fmt::{self, Display, Formatter};

#[derive(Debug, Clone)]
pub enum Tile {
    Empty,
    Wall,
    Floor,
}

impl Display for Tile {
    fn fmt(&self, f: &mut Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "{}",
            match self {
                Tile::Empty => " ",
                Tile::Wall => "#",
                Tile::Floor => ".",
            }
        )
    }
}
