import argparse
import sys
from tracker.fetcher import fetch_url
from tracker.parser import parse_html

# Create a parser
parser = argparse.ArgumentParser(description='Welcome to AutoPriceTracker CLI App')

# Add arguments
parser.add_argument(
    '--url', 
    default=None, 
    type=str,
    help='Url of your favorite product from an online e-commerce website'
)
parser.add_argument(
    '--target-price',
    default=None,
    type=float,
    help='Your target price for the product'
)

args = parser.parse_args()

# Call the app function to perform the fetch + parse logic 
html_text = fetch_url(args.url)
price = parse_html(html_text)

# Generate the user result and display on the terminal
if price and price <= args.target_price:
    print(f'Horray! current price:{price}, is less than or equal to your target price: {args.target_price}')
else:
    print(f'Sorry! current price: {price}, is still higher than your target price: {args.target_price}')