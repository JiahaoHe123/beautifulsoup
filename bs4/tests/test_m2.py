from bs4.filter import SoupReplacer, SoupStrainer
from bs4 import BeautifulSoup
import pytest

def _read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def test_task2():
  html = _read("apps/m2/test-files/large1.html")
  only_a = SoupStrainer("a")
  soup_filtered = BeautifulSoup(html, "html.parser", parse_only=only_a)
  soup_full = BeautifulSoup(html, "html.parser")
  a_filtered = [str(t) for t in soup_filtered]
  a_full = [str(t) for t in soup_full.find_all("a")]
  assert len(a_filtered) == len(a_full)


def test_task3():
  html = _read("apps/m2/test-files/large1.html")
  soup_filtered_all = BeautifulSoup(html, "html.parser",
                                    parse_only=SoupStrainer(True))
  soup_full = BeautifulSoup(html, "html.parser")

  filtered = [str(t) for t in soup_filtered_all.find_all(True)]
  full = [str(t) for t in soup_full.find_all(True)]

  assert len(filtered) == len(full)
  assert {t.name for t in soup_filtered_all.find_all(True)} == \
          {t.name for t in soup_full.find_all(True)}

def test_task4():
  html = _read("apps/m2/test-files/large1.html")

  soup_id_only = BeautifulSoup(html, "html.parser",
                                parse_only=SoupStrainer(id=True))
  soup_full = BeautifulSoup(html, "html.parser")

  # Collect elements that have id from each parse
  filtered_tags = soup_id_only.find_all(id=True)
  full_tags = soup_full.find_all(id=True)

  # Sanity: everything in the filtered parse must have an id
  assert all(t.has_attr("id") for t in filtered_tags)

  # Compare by identity features, not count/position
  filtered_pairs = {(t.name, t.get("id")) for t in filtered_tags}
  full_pairs = {(t.name, t.get("id")) for t in full_tags}

  assert filtered_pairs == full_pairs

def test_task6():
  with open("apps/m2/test-files/small4.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser", replacer=SoupReplacer("b", "blockquote"))
  assert soup.find("b") is None
  blockquotes = soup.find_all("blockquote")
  assert len(blockquotes) > 0
  for bq in blockquotes:
    assert bq.name == "blockquote"

if __name__ == "__main__":
    import pytest, sys
    sys.exit(pytest.main([__file__]))