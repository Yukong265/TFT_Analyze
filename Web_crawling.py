import requests
from bs4 import BeautifulSoup

url = r'http://127.0.0.1:5500/web.html'
req = requests.get(url)

decks = []
winning = []

if req.status_code == requests.codes.ok:
    soup = BeautifulSoup(req.content, 'html.parser')

else:
    print('failed')