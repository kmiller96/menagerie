mod area;
mod room;
mod tile;
mod utils;

// -------------------- //
// -- Display Module -- //
// -------------------- //

mod graphics {
    use crate::area::Area;

    const HORIZONTAL_BORDER_STRING: char = '-';
    const VERTICAL_BORDER_CHAR: char = '|';
    const CORNER_BORDER_CHAR: char = '+';

    /// Renders the map to the screen.
    pub fn render(area: Area) {
        // Get dimensions
        let (width, height) = area.dimensions();

        // Top border
        println!(
            "{}{}{}",
            CORNER_BORDER_CHAR,
            HORIZONTAL_BORDER_STRING.to_string().repeat(width as usize),
            CORNER_BORDER_CHAR
        );

        // Map rows
        for y in 0..height {
            print!("{}", VERTICAL_BORDER_CHAR);
            for x in 0..width {
                print!("{}", area[(x, y)]);
            }
            println!("{}", VERTICAL_BORDER_CHAR);
        }

        // Bottom border
        // TODO: Refactor to avoid code duplication with top border
        println!(
            "{}{}{}",
            CORNER_BORDER_CHAR,
            HORIZONTAL_BORDER_STRING.to_string().repeat(width as usize),
            CORNER_BORDER_CHAR
        );
    }
}

// --------------------- //
// -- Worldgen Module -- //
// --------------------- //

mod worldgen {
    use crate::area::Area;
    use crate::room::Room;

    // TODO: Make these randomly generated / supplied by the user.
    const MAP_WIDTH: u32 = 70;
    const MAP_HEIGHT: u32 = 18;

    pub fn generate(seed: u32) -> Area {
        let mut area = Area::new((MAP_WIDTH, MAP_HEIGHT));
        let room = Room::new((3, 3));

        area.blit(&room.area(), (1, 1));

        area
    }
}

// ------------------ //
// -- Main Routine -- //
// ------------------ //

fn main() {
    let map = worldgen::generate(0);
    graphics::render(map);
}
