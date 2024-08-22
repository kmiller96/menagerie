from loguru import logger
from requests import Response

from utils.preprocessing import preprocess


def parse(response: Response) -> tuple[int, int, int]:
    """Parses the message content from the response."""

    content = response.text
    logger.debug(f"Content: {content}")

    try:
        data = preprocess(content)
        logger.debug(f"Data: {data}")

    except ValueError as e:
        raise ValueError("Data misformatted.") from e

    return data
