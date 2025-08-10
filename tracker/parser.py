import re
from bs4 import BeautifulSoup

# Regex pattern for finding e.g. "$199.99" or "$ 5.0" from any given html page
pattern = re.compile(r"\$\s?(\d+(?:\.\d{1,2})?)")

"""
| Pattern       | Meaning                                                                                                                 |
| ------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `\$`          | Match a **literal dollar sign** (`$`). We escape it with `\` because `$` in regex means “end of string” unless escaped. |
| `\s?`         | Match **zero or one whitespace** character (space, tab, etc.). This accounts for both `$199` and `$ 199`.               |
| `(` `...` `)` | **Capturing group** — whatever matches inside will be returned by `.group(1)`.                                          |
| `\d+`         | Match **one or more digits** (`0-9`). This is the integer part of the price.                                            |
| `(?: ... )`   | **Non-capturing group** — groups the decimal part but doesn’t make it a separate capture.                               |
| `\.`          | Match a literal **dot** (`.`) — escaped so it’s not “any character”.                                                    |
| `\d{1,2}`     | Match **exactly 1 or 2 digits** after the dot. This enforces typical price formats like `.5` or `.50`.                  |
| `)?`          | The `?` after the group means **the entire decimal part is optional** — so it matches `$199` or `$199.99`.              |
"""


def parse_html(text):
    # Find and return the price from the given text
    soup = BeautifulSoup(text, "html.parser")

    if soup.html and soup.body:
        match = pattern.search(soup.text)
        if match:
            result = float(match.group(1))
            return result
        else:
            print(f"Unable to find price: Result is {match}")
    else:
        print(f"Invalid input: html:{soup.html}, body: {soup.body}")
