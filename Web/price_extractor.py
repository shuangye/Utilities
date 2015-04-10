# to parse prices

import sys
import os
import re
import requests
from bs4 import BeautifulSoup

def parse_page(url, price_id):
    if (None == url or None == price_id):
        return

    response = requests.get(url)
    if (requests.codes.ok != response.status_code):
        return

    soup = BeautifulSoup(response.text)
    price = soup.find(id = price_id)
    if (None != price):
        price_pattern = r'\d+(\.\d+)?'
        match = re.search(price_pattern, price.string)
        if (None != match):
            print('Title: {0}'.format(soup.title.string))
            print('Price: {0}'.format(match.group(0)))

def extract_url(seed):
    if (None == seed):
        return
        
    response = requests.get(seed)
    if (requests.codes.ok != response.status_code):
        return
        
    soup = BeautifulSoup(response.text)
    # href="/gp/product/B00BV656OW/
    amazon_product_link_pattern = r'[a-z]p/(product/)?\w{9,}/.*'
    prog = re.compile(amazon_product_link_pattern, re.IGNORECASE)
    for anchor in soup.find_all('a'):
        link = anchor.get('href')
        if (None != link):
            # print(link)
            match = prog.search(link)
            if (None != match):
                # print(match.group(0))
                url = os.path.join(r'http://www.amazon.cn/', match.group(0))
                parse_page(url, 'priceblock_ourprice')
                # extract_url(url)

# test();
# parse_page('http://www.amazon.cn/gp/product/B00QLU4AXG', 'priceblock_ourprice')
extract_url('http://www.amazon.cn/gp/product/B00QLU4AXG')
print('Done')

 
