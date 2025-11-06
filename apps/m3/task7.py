from bs4 import SoupReplacer, BeautifulSoup
from sys import argv

def change_class_to_test(tag):
  if tag.name == 'p':
    tag.attrs['class'] = 'test'

replacer = SoupReplacer(xformer=change_class_to_test)
path = argv[1]
with open(path) as f:
  soup = BeautifulSoup(f, 'html.parser', replacer=replacer)

output_path = 'output-file/' + 'changed-class-' + path[path.rfind('/')+1:]

with open(output_path, 'w') as f:
  f.write(soup.prettify())