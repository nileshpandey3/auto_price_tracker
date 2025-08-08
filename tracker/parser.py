import re
from bs4 import BeautifulSoup


def parse_html(text):
    soup = BeautifulSoup(text, 'html.parser')

    # Now we need to find the price component from the html page

    match = re.search(r"\$\s?(\d+(?:\.\d{1,2})?)", soup.get_text())
    if match:
        return float(match.group(1))
    
    