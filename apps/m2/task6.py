from bs4 import SoupReplacer, BeautifulSoup
from sys import argv

r = SoupReplacer('b', 'blockquote')

with open(argv[1], "r") as f:
  soup = BeautifulSoup(f, "html.parser", replacer=r)

print(soup.prettify())