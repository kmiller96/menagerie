mod app;
mod calculator;

use app::App;

fn main() {
    let mut app = App::new();
    app.run();
}
