mod worldgen;

// -------------------- //
// -- Display Module -- //
// -------------------- //

mod graphics {
    use super::worldgen::Map;

    /// Renders the map to the screen.
    pub fn render(map: Map) {
        println!("<<< TODO >>>");
    }
}

// ------------------ //
// -- Main Routine -- //
// ------------------ //

fn main() {
    let map = worldgen::generate(0);
    graphics::render(map);
}
