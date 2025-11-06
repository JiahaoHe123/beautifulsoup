from bs4.filter import SoupReplacer, SoupStrainer
from bs4 import BeautifulSoup
import pytest

def test_task7():
  def change_class_to_test(tag):
    if tag.name == 'p':
      tag.attrs['class'] = 'test'

  replacer = SoupReplacer(xformer=change_class_to_test)
  with open('apps/m2/test-files/large1.html') as f:
    soup = BeautifulSoup(f, 'html.parser', replacer=replacer)
  for tags in soup.find_all('p'):
    assert tags.attrs['class'] == 'test'

  with open('apps/m2/test-files/large1.html') as f2:
    soup2 = BeautifulSoup(f2, 'html.parser', replacer=replacer)
  for tags in soup.find_all('p'):
    assert tags.attrs['class'] == 'test'

if __name__ == "__main__":
    import pytest, sys
    sys.exit(pytest.main([__file__]))