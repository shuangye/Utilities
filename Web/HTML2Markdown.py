import sys
import requests
from bs4 import BeautifulSoup


"""
To fetch the target
"""
def fetch_content(url):
    if (None == url):
        return

    response = requests.get(url)
    if (requests.codes.ok != response.status_code):
        return

    soup = BeautifulSoup(response.text)
    return soup


"""
guess the possible id of the main part
"""
def main_content_id(default, soup):
    if (None != default):
        return default
        
    # dict
    possible_content_ids = ('content', 'content-wrapper', 'main', 'main-content')
    # search possible IDs in the soup object


"""
To parse the HTML content, represented by a soup object
"""
def parse_content(soup, file_out, main_content_id):
    if (None == soup or None == file_out):
        return

    file_md = open(file, 'w')
    print('{0}\n'.format(soup.title), file = file_md)
    

"""
To download the referenced resources
"""
def download_res(res_url):
    if (None == res_url):
        return
    
trade_spider(8)
