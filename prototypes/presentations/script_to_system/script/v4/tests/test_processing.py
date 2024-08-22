"""Runs tests for the processing script."""

from unittest.mock import Mock

import requests
import pytest

from eureka4.processing import parse


def test_parse_when_good_response():
    """Should return the parsed data."""
    data = (0, 0, 1)

    response = Mock(requests.Response)
    response.text = f"{data[0]},{data[1]},{data[2]}"

    assert data == parse(response)


def test_parse_when_bad_response():
    """Should raise an error."""
    response = Mock(requests.Response)
    response.text = "bad data"

    with pytest.raises(ValueError):
        parse(response)


def test_parse_when_response_empty():
    """Should raise an error."""
    response = Mock(requests.Response)
    response.text = "bad data"

    with pytest.raises(ValueError):
        parse(response)


def test_parse_when_wrong_types():
    """Should raise an error."""
    response = Mock(requests.Response)
    response.text = "a,b,c"

    with pytest.raises(ValueError):
        parse(response)
