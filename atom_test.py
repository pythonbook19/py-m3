


import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_html(url):
    r = requests.get(url)
    return r

def main():
    url = 'http://www.offshore-mag.com/all-offshore-articles.html'

    print(get_html(url).text)

if __name__ == '__main__':
    main()
