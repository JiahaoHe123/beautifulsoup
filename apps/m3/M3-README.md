# Milestone-3

## Environment
```bash
beautifulsoup:~/ python3 -m venv venv
```
```bash
beautifulsoup:~/ source venv/bin/activate
```

## What is new

Add some new functionality for `SoupReplacer`.

This milestone generalizes the M2 “simple replace” into a flexible transformer
API that can rename tags, rewrite attributes, or perform arbitrary side effects

- What’s new vs M2
	- M2: simple pair replacement (e.g., replace every `<b>` with `<blockquote>`).
	- M3: transformer callbacks applied during parsing:
		- `name_xformer(tag) -> str` to set a new tag name
		- `attrs_xformer(tag) -> dict` to replace a tag’s attributes
		- `xformer(tag) -> None` for arbitrary side effects on the `Tag`
	- The M2 functionality is preserved (`og_tag`, `alt_tag`).


### New constructor

```python
from bs4.filter import SoupReplacer

SoupReplacer(
		og_tag: str | None = None,
		alt_tag: str | None = None,
		*,
		name_xformer: callable | None = None,
		attrs_xformer: callable | None = None,
		xformer: callable | None = None,
)
```

## What it does

1) M2-style: replace `<b>` with `<blockquote>`

    ```python
    from bs4 import BeautifulSoup
    from bs4.filter import SoupReplacer

    html = "<p>Hello <b id='x'>world</b>!</p>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    print(str(soup))  # <p>Hello <blockquote id="x">world</blockquote>!</p>
    ```

2) Rename tags with `name_xformer`

    ```python
    def to_strong(tag):
        return "strong" if tag.name == "b" else tag.name

    replacer = SoupReplacer(name_xformer=to_strong)
    soup = BeautifulSoup("<p><b>Bold</b></p>", "html.parser", replacer=replacer)
    ```

3) Remove all `class` attributes with `attrs_xformer`

    ```python
    def drop_class(tag):
        new_attrs = dict(tag.attrs)
        new_attrs.pop("class", None)
        return new_attrs

    replacer = SoupReplacer(attrs_xformer=drop_class)
    soup = BeautifulSoup(
      "<p class='intro'><span class='hi'>x</span></p>",
      "html.parser", replacer=replacer
    )
    ```

4) Add a data flag to every `<p>` with `xformer`

    ```python
    def add_flag(tag):
      if tag.name == "p":
        tag.attrs["data-flag"] = "yes"

    replacer = SoupReplacer(xformer=add_flag)
    soup = BeautifulSoup(
      "<div><p>A</p><p>B</p></div>",
      "html.parser",
      replacer=replacer
    )
    ```

5) Combine transformers

    ```python
    def name_x(tag):
        return "strong" if tag.name == "b" else tag.name

    def attrs_x(tag):
        new_attrs = dict(tag.attrs)
        new_attrs.pop("class", None)
        return new_attrs

    replacer = SoupReplacer(
      name_xformer=name_x,
      attrs_xformer=attrs_x
    )
    soup = BeautifulSoup(
      "<p><b class='c'>Bold</b></p>",
      "html.parser",
      replacer=replacer
    )
    ```

## Where the code lives
  - `bs4/filter.py`: Modified constructor of `SoupReplacer`
    (modeled after `SoupStrainer`). (**684 - 756**)
  stores it on the soup instance.(**94, 216, 374**)
  - `bs4/builder/_htmlparser.py`: in `handle_starttag(...)`(**189 - 190**),
    ```python
    if replacer and callable(replacer) and tag is not None:
      replacer(tag)
    ```

## How to run

### Run the tests for SoupReplacer

From the repository root:

```bash
python3 bs4/tests/test_replacer.py
```

### task7.py

adding (or replacing) a `class` attribute to `class="test"` for all `<p>`
tags in an `HTML` file and print out the **prettified** `soup` to
a new file

```bash
cd apps/m3
```
```bash
python3 task7.py <path to file>
```

**output path**:
`apps/m3/output-file/changed-class-<file name>`

#### Example
```bash
python3 task7.py ../m2/test-files/small4.html
```
**output file path**:
`apps/m3/output-file/changed-class-small4.html`

### Test for task7.py

From the root run the following:
```bash
python3 bs4/tests/test_m3.py
```