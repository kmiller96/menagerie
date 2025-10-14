pub enum Characters {
    HorizontalBar,
    VerticalBar,
    RightDown,
    LeftDown,
    RightUp,
    LeftUp,
    TeeLeft,
    TeeRight,
    TeeUp,
    TeeDown,
}

impl Characters {
    pub fn as_str(&self) -> &str {
        match self {
            Characters::HorizontalBar => "═",
            Characters::VerticalBar => "║",
            Characters::RightDown => "╔",
            Characters::LeftDown => "╗",
            Characters::RightUp => "╚",
            Characters::LeftUp => "╝",
            Characters::TeeLeft => "╠",
            Characters::TeeRight => "╣",
            Characters::TeeUp => "╩",
            Characters::TeeDown => "╦",
        }
    }
}
