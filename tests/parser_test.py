import pytest

from tracker.parser import parse_html


@pytest.mark.parser
class TestParser:
    @pytest.mark.validate_parser
    def test_valid_html_input(self):
        html = "<html><body>Price is $9.99</body></html>"
        result = parse_html(html)
        assert result == 9.99

    @pytest.mark.invalid_input
    def test_invalid_input(self, capfd):
        html = "invalid"
        result = parse_html(html)
        (out, err) = capfd.readouterr()
        assert result is None
        assert "Invalid input: html:None, body: None" in out

    @pytest.mark.wrong_currency
    def test_wrong_currency(self, capfd):
        html = "<html><body>Price is CAD #$#.99</body></html>"
        parse_html(html)
        (out, err) = capfd.readouterr()
        assert "Unable to find price: Result is None" in out
