import re
from bs4 import BeautifulSoup

# Regex pattern for finding e.g. "$199.99" or "$ 5.0"
pattern = re.compile(r"\$\s?(\d+(?:\.\d{1,2})?)")

def parse_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    match = pattern.search(soup.text)
    if match:
        return float(match.group(1))
    
