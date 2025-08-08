import argparse
import sys
from tracker.fetcher import fetch_url
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
    type=int,
    help='Your target price for the product'
)

args = parser.parse_args()


fetch_url(args.url)