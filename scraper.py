'''Module to extract the data'''
import requests
from bs4 import BeautifulSoup

def extract_other_pages(url):
    # Make an HTTP request to the homepage of the website
    response = requests.get(url)
    html = response.text

    # Parse the HTML of the homepage
    soup = BeautifulSoup(html, 'html.parser')

    # Extract all the links from the homepage
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))

    # Find the links to the other pages
    other_pages = []
    sub_url = url.replace('https://', '')
    if 'www.' in url:
        sub_url = sub_url.replace('www.', '')
        list1 = sub_url.split('/')
        url_to = ''.join(list1[:1])
    for link in links:
        if link:
            if sub_url in link:
                other_pages.append(link)
            elif link.startswith('/'):
                test = 'https://' + url_to + link
                other_pages.append(test)

    # Remove duplicates from the list of other pages
    other_pages = list(set(other_pages))
    return other_pages

def requests_extract_soup(url):
    response = requests.get(url)
    html = response.text

    # Parse the HTML of the homepage
    soup = BeautifulSoup(html, 'html.parser')

    return soup