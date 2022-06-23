import requests
from bs4 import BeautifulSoup
import re
import matplotlib as plt

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

    
for i in range(2,33):
    if i == 7:
        continue
    win = str(soup.select(f'#decks > div > section:nth-child(4) > div.col-12.col-xl-9 > div:nth-child({i}) > div > div.deck__stats > dl:nth-child(1) > dd'))
    per = re.sub('<.+?>',"", win)
    r = ''
    for i in range(1,5):
        r += per[i]
    winning.append(float(r))

result = {}

for i in range(30):
    result.setdefault(decks[i], winning[i])

key = list(result.keys())
value = list(result.values())

plt.rc('font', family='Malgun Gothic', size=6)
plt.bar(key,value)
plt.xticks(rotation=45)
plt.show()