import pytest

from tracker.fetcher import fetch_url


@pytest.mark.fetcher
class TestFetcher:
    @pytest.mark.example_url
    def test_successful_fetch_with_example_url(self):
        url = "https://example.com"
        resp = fetch_url(url)
        assert "Example Domain" in resp

    @pytest.mark.empty_url
    def test_empty_url(self, capfd):
        fetch_url("")
        (out, err) = capfd.readouterr()
        assert "Invalid URL '': No scheme supplied. Perhaps you meant https://?" in out

    @pytest.mark.invalid_url
    def test_invalid_url(self, capfd):
        fetch_url("someinvalidurl.com")
        (out, err) = capfd.readouterr()
        assert (
            "Invalid URL 'someinvalidurl.com': No scheme supplied. Perhaps you meant https://someinvalidurl.com?"
            in out
        )
