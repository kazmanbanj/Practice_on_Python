import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.nairaland.com/education')
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# print(soup.find(id='score_20514755'))
# print(soup.select('#score_20514755'))
# print(soup.select('.score'))

