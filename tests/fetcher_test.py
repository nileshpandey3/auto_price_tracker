import pytest, ipdb

from tracker.fetcher import fetch_url

@pytest.mark.fetcher
class TestFetcher:

    @pytest.mark.validate_url
    def test_validate_url(self):
        url = 'https://example.com'
        resp = fetch_url(url)
        assert isinstance(resp, str)
        