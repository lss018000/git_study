import requests
from bs4 import BeautifulSoup
import pandas as pandas
resp = requests.get('')
html = resp.text
soup = BeautifulSoup(html, 'html.parser')
news = soup.select('.search_result')