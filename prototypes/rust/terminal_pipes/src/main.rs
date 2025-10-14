mod coordinate;
mod map;
mod pipe;

use map::Map;
use pipe::Pipe;

const XDIM: u16 = 10;
const YDIM: u16 = 10;

fn main() -> std::io::Result<()> {
    let map = Map::new(XDIM, YDIM);

    for _ in 0..5 {
        // Initialise pipe
        let start = map.random_start_coordinate();
        let mut pipe = Pipe::new(start);

        println!(
            "Created pipe starting at: ({}, {})",
            pipe.start().x,
            pipe.start().y
        );

        // Grow
        loop {
            pipe.grow();

            let end = pipe.end();
            if !map.contains(&end) {
                break;
            }
        }

        // Print segments
        for segment in pipe.segments {
            println!("Segment at: ({}, {})", segment.x, segment.y);
        }
    }

    Ok(())
}
