mod map;
mod tile;
mod utils;

// -------------------- //
// -- Display Module -- //
// -------------------- //

mod graphics {
    use crate::map::Map;

    /// Renders the map to the screen.
    pub fn render(map: Map) {
        // println!("{}", map);
    }
}

// --------------------- //
// -- Worldgen Module -- //
// --------------------- //

mod worldgen {
    use crate::map::Map;
    use crate::tile::{Tile, TileType};

    // TODO: Make these randomly generated / supplied by the user.
    const MAP_WIDTH: u32 = 5;
    const MAP_HEIGHT: u32 = 5;

    pub fn generate(seed: u32) -> Map {
        let mut map = Map::new(MAP_WIDTH, MAP_HEIGHT);

        map[(0, 0)] = Tile {
            value: TileType::Wall,
            position: (0, 0),
        };
        map[(0, 1)] = Tile {
            value: TileType::Floor,
            position: (0, 1),
        };
        map[(0, 2)] = Tile {
            value: TileType::Empty,
            position: (0, 2),
        };

        println!("{}", &map);

        map
    }
}

// ------------------ //
// -- Main Routine -- //
// ------------------ //

fn main() {
    let map = worldgen::generate(0);
    graphics::render(map);
}
