from bs4 import SoupStrainer, BeautifulSoup
from sys import argv

only_tags_with_id = SoupStrainer(id=True)

with open(argv[1], "r") as f:
  soup = BeautifulSoup(f, "html.parser", parse_only=only_tags_with_id)

for tag in soup.find_all(id=True):
    print(tag)
