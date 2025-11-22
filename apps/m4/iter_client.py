from bs4 import BeautifulSoup
from sys import argv

path = argv[1]

with open(path) as f:
  soup = BeautifulSoup(f, 'html.parser')

for node in soup:
  print(node)
