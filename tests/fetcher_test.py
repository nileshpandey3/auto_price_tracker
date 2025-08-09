import pytest

@pytest.mark.fetcher
class TestFetcher:

    @pytest.mark.validate_url
    def test_validate_url(self):
        pass