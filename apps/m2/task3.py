from bs4 import SoupStrainer, BeautifulSoup
from sys import argv

all_tags = SoupStrainer(True)

with open(argv[1], "r") as f:
  soup = BeautifulSoup(f, "html.parser", parse_only=all_tags)

for tag in soup:
  print(tag.name)