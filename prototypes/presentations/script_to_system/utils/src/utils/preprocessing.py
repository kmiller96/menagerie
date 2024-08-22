def preprocess(content: str) -> tuple[int, int, int]:
    """Preprocesses the response content."""
    x, y, in_circle = content.split(",")
    return int(x), int(y), int(in_circle)
