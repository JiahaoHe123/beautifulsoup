from bs4 import BeautifulSoup
from bs4.element import NavigableString
import pytest

def test_iter_simple_html():
  html = "<div><p>a</p><p>b</p></div>"
  soup = BeautifulSoup(html, "html.parser")
  tag_names = [
    getattr(node, "name")
    for node in soup
    if getattr(node, "name") is not None
  ]
  assert tag_names == ["[document]", "div", "p", "p"]

def test_iter_nested_structure():
  html = "<div><span><b>hi</b></span><span>there</span></div>"
  soup = BeautifulSoup(html, "html.parser")
  tag_names = [
    getattr(node, "name")
    for node in soup
    if getattr(node, "name") is not None
  ]
  assert tag_names == ["[document]", "div", "span", "b", "span"]

def test_iter_includes_text_nodes():
  html = "<p>Hello <b>bold</b> world</p>"
  soup = BeautifulSoup(html, "html.parser")
  texts = [
    str(node).strip()
    for node in soup
    if isinstance(node, NavigableString) and str(node).strip() != ""
  ]
  assert texts == ["Hello", "bold", "world"]

def test_iter_single_closing_tag():
  html = "<br/>"
  soup = BeautifulSoup(html, "html.parser")
  tag_names = [
    getattr(node, "name")
    for node in soup
    if getattr(node, 'name') is not None
  ]
  assert tag_names == ["[document]", "br"]

def test_iter_sequence_for_multiple_layers():
  html = """
    <section id="s1">
        <h1>One</h1>
        <p>P1</p>
    </section>
    <section id="s2">
        <h1>Two</h1>
        <p>P2</p>
    </section>
    """
  soup = BeautifulSoup(html, "html.parser")
  tag_names = [
    getattr(node, "name")
    for node in soup
    if getattr(node, 'name') is not None
  ]
  subseq = [name for name in tag_names if name in ("section", "h1", "p")]
  assert subseq == [
    "section", "h1", "p",
    "section", "h1", "p"
  ]

def test_iter_multiple_sections():
  html = """
    <body>
      <section id="s1"><p>One</p></section>
      <section id="s2"><p>Two</p></section>
    </body>
    """

  soup = BeautifulSoup(html, "html.parser")

  tag_names = [node for node in soup]

  sections = [
    node
    for node in tag_names
    if getattr(node, "name") == "section"
  ]

  assert len(sections) == 2
  assert sections[0]["id"] == "s1"
  assert sections[1]["id"] == "s2"

def test_soup_after_iter():
  html = """
    <body>
      <section id="s1"><p>One</p></section>
      <section id="s2"><p>Two</p></section>
    </body>
    """
  soup = BeautifulSoup(html, "html.parser")
  sections_before_iter = [tag["id"] for tag in soup.find_all("section")]
  for _ in soup:
    continue
  sections_after_iter = [tag["id"] for tag in soup.find_all("section")]
  assert sections_before_iter == ['s1', 's2']
  assert sections_after_iter == ['s1', 's2']
  assert sections_after_iter == sections_before_iter

if __name__=='__main__':
  import sys
  sys.exit(pytest.main([__file__]))