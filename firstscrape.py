import urllib.request, urllib.parse, urllib.error
from beautifulsoup4 import BeautifulSoup
html = urllib.request.urlopen(page).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))