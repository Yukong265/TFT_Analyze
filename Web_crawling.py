import requests
from bs4 import BeautifulSoup
import re

url = r'http://127.0.0.1:5500/web.html'
req = requests.get(url)

decks = []
winning = []

if req.status_code == requests.codes.ok:
    soup = BeautifulSoup(req.content, 'html.parser')

else:
    print('failed')

for i in range(2,33):
    if i == 7:
        continue
    rst = str(soup.select(f'#decks > div > section:nth-child(4) > div.col-12.col-xl-9 > div:nth-child({i}) > header > h4 > a > b'))
    r = re.sub('<.+?>',"", rst)
    deck = r.lstrip('[').rstrip(']')

    decks.append(deck)