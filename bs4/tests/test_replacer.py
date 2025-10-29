from bs4.filter import SoupReplacer

import pytest
from bs4 import BeautifulSoup

def test_b_to_blockquote_simple():
    html = "<p>Hello <b id='x'>world</b>!</p>"
    soup = BeautifulSoup(html, "html.parser", replacer=SoupReplacer("b", "blockquote"))
    assert str(soup) == '<p>Hello <blockquote id="x">world</blockquote>!</p>'
    assert soup.find("b") is None
    bb = soup.find("blockquote")
    assert bb and bb.get("id") == "x" and bb.text == "world"

def test_nested_and_mixed_case():
    html = "<DIV><B>A <b>B</b></B></DIV>"
    soup = BeautifulSoup(html, "html.parser", replacer=SoupReplacer("b", "blockquote"))
    assert str(soup) == '<div><blockquote>A <blockquote>B</blockquote></blockquote></div>'
    assert soup.find("b") is None
    assert len(soup.find_all("blockquote")) == 2

def test_p_to_div_with_attributes():
    with open("apps/m2/test-files/small4.html", "r") as f:
      soup = BeautifulSoup(f, "html.parser", replacer=SoupReplacer("p", "div"))
    div = soup.find("div")
    assert div is not None
    assert soup.find("p") is None

if __name__ == "__main__":
    import pytest, sys
    sys.exit(pytest.main([__file__]))