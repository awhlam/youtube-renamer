import urllib.request as urllib
from bs4 import BeautifulSoup
import re

URLS = [
  'https://www.youtube.com/watch?v=56OJJTxCEN4',
  'https://www.youtube.com/watch?v=dGcsHMXbSOA',
  'https://www.youtube.com/watch?v=bPPiuludHKg'
]

def getTitle(url):
  soup = BeautifulSoup(urllib.urlopen(url), 'lxml')
  title = soup.title.string
  title = re.sub(' - YouTube$', '', title)
  return title

if __name__ == "__main__":
  for url in URLS:
    print(getTitle(url))