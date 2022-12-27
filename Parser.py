import requests
from bs4 import BeautifulSoup as bs


def parser(url):
    """
    Parses the page and returns and returns the current version from the page
    :param url: string
    :return: string
    """
    r = requests.get(url)
    html = r.text
    soup = bs(html, 'html.parser')
    version = soup.find_all('div', class_="")
    return version[0].text
