from utilities.url_utilities import load_urls_from_file
import logging

LOGGER = logging.getLogger(__name__)


def test_load_file():
    LOGGER.info("Running test")
    test_urls = load_urls_from_file("input.txt")
    assert (len(test_urls) > 1)
