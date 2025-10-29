# Milestone-2

  This project has **three** parts:
  - Part 1:
    - Task2: Use `SoupStrainer` to find out all `<a>` tags in a given
    `html/xml` file.
    - Task3: Use `SoupStrainer` to find out all tags in a given `html/xml` file.
    - Task4: Use `SoupStrainer` to find out all tags with an `id` attribute
    in a given `html/xml` file.
  - Part 2:
    - Locate the exact files/lines of the definitions of **ALL** the API
    functions we used in **Milestone 1** and in **Part-1** of **Milestone-2**.
  - Part 3:
    - Build new API `SoupReplacer`: parse-time tag replacement
    (currently only htmlparser)
    - Use new build `SoupReplacer` to do the `task6.py` in **Milestron-1**

## Part 1

### task2.py

Exercise printing out all hyperLinks in a HTML/XML file using `SoupStrainer`.

**Input**: a path to an HTML/XML file.<br>
**Output**: All hyperLinks in the input file printed out on console

### To run the code on terminal, follow the following instruction:
- If you are currently in `beautifulsoup/apps/m2` directory, do the following
  ```bash
  python3 task2.py <path-to-file>
  ```
- If you are not in `beautifulsoup/apps/m2` directory, do the following
  ```bash
  cd beautifulsoup/apps/m2
  python3 task2.py <path-to-file>
  ```

### Example
  ```bash
  python3 task2.py test-files/large1.html
  ```
  **Output**: All HyperLinks(a tag) in the input file
              will be printed on console


### task3.py

Exercise printing out all tags in a HTML/XML file using `SoupStrainer`.


**Input**: a path to an HTML/XML file.<br>
**Output**: All tags in the input file printed out on console.

### To run the code on terminal, follow the following instruction:
- If you are currently in `beautifulsoup/apps/m2` directory, do the following
  ```bash
  python3 task3.py <path-to-file>
  ```
- If you are not in `beautifulsoup/apps/m2` directory, do the following
  ```bash
  cd beautifulsoup/apps/m2
  python3 task3.py <path-to-file>
  ```

### Example
  ```bash
  python3 task3.py test-files/large1.html
  ```
  **Output**: All tags in given file will be printed on console.


## task4.py

  Exercise printing out all tags with id in a HTML/XML file using
  `SoupStrainer`.

**Input**: a path to an HTML/XML file.<br>
**Output**: All tags with id in the input file printed out on console.

### To run the code on terminal, follow the following instruction:
- If you are currently in `beautifulsoup/apps/m2` directory, do the following
  ```bash
  python3 task4.py <path-to-file>
  ```
- If you are not in `beautifulsoup/apps/m2` directory, do the following
  ```bash
  cd beautifulsoup/apps/m2
  python3 task4.py <path-to-file>
  ```

### Example
  ```bash
  python3 task4.py test-files/large1.html
  ```
  **Output**: All tags with id in given file will be printed on console.

### test all tasks
  - Run the following if you are in the beautiful directory:
  ```bash
  python3 bs4/tests/test_m2.py
  ```

## Part 2

### M1
- **Class Constructors**
  - `BeautifulSoup()`: `beautifulsoup/bs4/__init__.py`： **209 - 490** with
  `param markup = <input_file>, param features = <kind of parser>`.

- **task1.py in M1**: `soup.prettify()`
  - `prettify()`: `beautifulsoup/bs4/element.py`: **2601 - 2617**.
- **task2.py in M1**: `soup.find_all('a')`
  - `find_all(name)`: `beautifulsoup/bs4/element.py`: **2715 - 2745** with
  `param name = 'a'`.
- **task3.py in M1**: `soup.find_all(True)`
  - `find_all(recursive)` : `beautifulsoup/bs4/element.py`: **2715 - 2745**
  with `param recursive = True`.
- **task4.py in M1**: `soup.find_all(id=True)`
  - `find_all(attrs)`: `beautifulsoup/bs4/element.py`: **2715 - 2745** with
  `param attrs = {id: True}`.
- **task5.py in M1**: `tag.find_parents()`, `soup.find_all()`
  - `find_parents()`: `beautifulsoup/bs4/element.py`: **1022 - 1044**.
  - `find_all()`: `beautifulsoup/bs4/element.py`: **2715 - 2745**.
- **task6.py in M1**: `soup.find_all('b')`, `soup.prettify()`
  - `find_all(name)`: `beautifulsoup/bs4/element.py`: **2715 - 2745** with
  `param name = 'a'`.
  - `prettify()`: `beautifulsoup/bs4/element.py`: **2601 - 2617**.
- **task7.py in M1**: `soup.find_all('p')`, `soup.prettify()`
  - `find_all(name)`: `beautifulsoup/bs4/element.py`: **2715 - 2745** with
  `param name = 'a'`.
  - `prettify()`: `beautifulsoup/bs4/element.py`: **2601 - 2617**.
- **task8.py in M1**: `soup.find_all('p')`, `soup.new_tag('div')`,
`new_div.extend(p)`, `p.insert_after(new_div)`, `p.decompose()`,
`soup.prettify()`
  - `find_all(name)`: `beautifulsoup/bs4/element.py`: **2715 - 2745** with
  `param name = 'p'`.
  - `new_tag(name)`: `beautifulsoup/bs4/__init__.py`: **682 - 730** with
  `param name = 'div'`.
  - `extend(tags)`: `beautifulsoup/bs4/element.py`: **2056 - 2091** with
  `param tags = <p tag>`(moves `p.content` to into `new_div`).
  - `insert_after(args)`: `beautifulsoup/bs4/element.py`: **716 - 745** with
  `param args = <div tag>`(new created div element).
  - `decompose()`: `beautifulsoup/bs4/element.py`: **635 - 655**.
  - `prettify()`: `beautifulsoup/bs4/element.py`: **2601 - 2617**.

### M2
- **Class Constructo**
  - `BeautifulSoup()`:  `beautifulsoup/bs4/__init__.py`： **209 - 490** with
  `param markup = <input_file>, param features = <kind of parser>, `
  `param parse_only = <SoupStrainer>`.
  - `SoupStrainer()`: `beautifulsoup/bs4/filter.py`: **345 - 396** with
  `param name = <tag name> | attrs = <{attrs of tag}>`.

## Part 3
  SoupReplacer: parse-time tag replacement(currently only htmlparser)

  The design mirrors SoupStrainer: you pass a SoupReplacer object into the
  BeautifulSoup(...) constructor via the replacer= keyword.
  - **what it does**
    ```python
    from bs4 import BeautifulSoup
    from bs4.filter import SoupReplacer

    b_to_blockquote = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html_doc, "html.parser", replacer=b_to_blockquote)
    print(soup.prettify())
    ```

    All `<b>` tags are emitted as `<blockquote>` in the final tree, and
    attributes/contents are preserved.

  - **Where the code lives**
    - `bs4/filter.py`: Added class `SoupReplacer`
    (modeled after `SoupStrainer`). (**694 - 704**)
    - `bs4/__init__.py`: `BeautifulSoup.__init__` now accepts `replacer=` and
    stores it on the soup instance.(**94, 216, 374**)
    - `bs4/builder/_htmlparser.py`: in `handle_starttag(...)`(**155 - 158**),
    `handle_endtag(...)`(**216 - 219**) before creating the `Tag`, apply:
      ```python
      replacer = getattr(self.soup, "replacer", None)
      if replacer is not None:
        name = replacer.change(name)
      ```

  - **Test**
    - File: `bs4/tests/test_replacer.py`

      Run the following if you are in the beautifulsoup directory:
      ```bash
      python3 bs4/tests/test_replacer.py
      ```
  - **Application for Task-6**
    - Goal: “Change all the `<b>` tags to `<blockquote>` tags and print the
    tree to the console.”
    - File: `apps/m2/task6.py`
