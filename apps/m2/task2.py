from bs4 import SoupStrainer, BeautifulSoup
from sys import argv

only_a_tags = SoupStrainer("a")
path = argv[1]
with open(path, "r") as f:
  soup = BeautifulSoup(f, "html.parser", parse_only=only_a_tags)

for s in soup:
  print(s)