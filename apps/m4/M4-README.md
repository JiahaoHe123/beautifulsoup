# Milestone-4

## Environment
```bash
beautifulsoup:~/ python3 -m venv venv
```
```bash
beautifulsoup:~/ source venv/bin/activate
```

## What is new

The `BeautifulSoup` object is now iterable!
By having this, the soup is now iterable. We can now iterate
over all of its nodes.

## New Function

```python
    def __iter__(self):
        stack = [self]
        while stack:
            node = stack.pop()
            yield node
            if hasattr(node, 'contents'):
                for child in reversed(node.contents):
                    stack.append(child)
```

## What it does

1) Define a `__iter__` function, which will make python "know"
the object is iterable. Then we can use `for loop` or `while loop`
to iterate the soup object.

2) This iter will perform a DFS(Deepth first search) by using a
stack, visits the current node, pushes children in reverse order
so the natural order appears correct, and yields each node exactly once.

## Where the code lives
- `bs4/__init__.py`: Add a function called `__iter__` right after
the constructor of soup(**495 - 502**)

## How to use it

### Client side code example

```python
with open(path) as f:
  soup = BeautifulSoup(f, 'html.parser')

for node in soup:
  print(node)
```

- Run the client code
  from the repository root:
  ```bash
  python3 apps/m4/iter_client.py <path-to-file>
  ```

  Example to run:
  ```bash
  apps/m4/iter_client.py apps/m2/test-files/small4.html
  ```

- (The above code lives in `apps/m4/iter_clinet.py`)

### Run the tests code

From the repository root:
```bash
python3 bs4/tests/test_iter.py
```