import requests

from eureka.exceptions import BadResponseError


def fetch(url: str) -> requests.Response:
    """Retrieves the data from the URL."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

    except requests.Timeout as e:
        raise BadResponseError("Request timed out.") from e

    except requests.exceptions.HTTPError as e:
        raise BadResponseError("HTTP error occurred.") from e

    else:
        return response
