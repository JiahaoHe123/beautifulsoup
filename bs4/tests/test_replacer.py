from bs4.filter import SoupReplacer
from bs4 import BeautifulSoup
import pytest

# Milestone 2 – original tests

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



# Milestone 3 – new behavior

def test_name_xformer_b_to_blockquote():
    html = "<p>Some <b>bold</b> and <i>italic</i> text.</p>"

    replacer = SoupReplacer(
        name_xformer=lambda tag: "blockquote" if tag.name == "b" else tag.name
    )

    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert soup.find("b") is None
    assert len(soup.find_all("blockquote")) == 1
    assert len(soup.find_all("i")) == 1  # <i> unchanged


def test_attr_xformer_remove_class():
    html = '<p class="intro">Hello <span class="hi" id="s1">world</span></p>'

    def remove_class(tag):
        new_attrs = dict(tag.attrs)
        if "class" in new_attrs:
            del new_attrs["class"]
        return new_attrs

    replacer = SoupReplacer(attrs_xformer=remove_class)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    for tag in soup.find_all(True):
        assert "class" not in tag.attrs


def test_xformer_side_effect_add_data_flag_to_p():
    html = "<div><p>First</p><p>Second</p><span>Other</span></div>"

    def add_flag(tag):
        if tag.name == "p":
            tag.attrs["data-flag"] = "yes"

    replacer = SoupReplacer(xformer=add_flag)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    for p in soup.find_all("p"):
        assert p.attrs.get("data-flag") == "yes"

    for s in soup.find_all("span"):
        assert "data-flag" not in s.attrs


def test_combined_name_and_attr_xformers():
    html = '<p><b class="c">Bold</b></p>'

    def name_x(tag):
        return "strong" if tag.name == "b" else tag.name

    def attrs_x(tag):
        new_attrs = dict(tag.attrs)
        new_attrs.pop("class", None)
        return new_attrs

    replacer = SoupReplacer(name_xformer=name_x, attrs_xformer=attrs_x)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert soup.find("b") is None
    strong_tags = soup.find_all("strong")
    assert len(strong_tags) == 1

    strong = strong_tags[0]
    assert "class" not in strong.attrs
    assert strong.text == "Bold"

def test_name_xformer_p_to_div_in_large_file():
    replacer = SoupReplacer(
        name_xformer=lambda tag: "div" if tag.name == "p" else tag.name
    )
    with open("apps/m2/test-files/large1.html") as f:
        soup = BeautifulSoup(f, "html.parser", replacer=replacer)
    with open("apps/m2/test-files/large1.html") as f:
        soup2 = BeautifulSoup(f, "html.parser")
    assert soup.find("p") is None
    assert soup2.find("p") is not None

def test_remove_all_class_in_large_file():
    def remove_all_classes(tag):
        tag.attrs.pop("class", None)

    replacer = SoupReplacer(
        xformer=remove_all_classes
    )

    with open("apps/m2/test-files/large1.html") as f:
        soup = BeautifulSoup(f, "html.parser", replacer=replacer)
    for tag in soup.find_all():
        assert "class" not in tag.attrs

def test_remove_all_attrs_in_large_file():
    def remove_all_attrs(tag):
        return {}

    replacer = SoupReplacer(
        attrs_xformer=remove_all_attrs
    )

    with open("apps/m2/test-files/large1.html") as f:
        soup = BeautifulSoup(f, "html.parser", replacer=replacer)
    for tag in soup.find_all():
        assert tag.attrs == {}

def test_name_xformer_for_multiple_tags():
    def replace_names(tag):
        replacements = {
            "p": "div",
            "b": "strong"
        }
        return replacements.get(tag.name, tag.name)
    replacer = SoupReplacer(name_xformer=replace_names)
    with open("apps/m2/test-files/large1.html") as f:
        soup = BeautifulSoup(f, "html.parser", replacer=replacer)
    assert soup.find('p') is None
    assert soup.find('b') is None

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
