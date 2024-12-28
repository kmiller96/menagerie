use crossterm::event::{self, Event};
use ratatui::{text::Text, Frame};

fn main() {
    let mut terminal = ratatui::init();
    loop {
        terminal.draw(draw).expect("failed to draw frame");
        if matches!(event::read().expect("failed to read event"), Event::Key(_)) {
            break;
        }
    }
    ratatui::restore();
}

fn draw(frame: &mut Frame) {
    let mut pos = frame.area();

    pos.x += 1;
    pos.y += 1;

    let text = Text::raw("Hello World!");
    frame.render_widget(text, pos);
}
