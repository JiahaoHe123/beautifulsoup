# Extending BeautifulSoup with SoupReplacer

## Background
SoupReplacer is an experimental API for transforming tags during parsing.
In Milestone 2, it supported only simple name replacement
(e.g. `SoupReplacer("b", "blockquote")`). In Milestone 3, it is extended to
support three transformer hooks: `name_xformer`, `attrs_xformer`,
and `xformer`, each operating on `Tag` objects directly.

## Milestone 2
- **API**: `SoupReplacer(og_tag, alt_tag)`.
- **Strengths**: simple and easy to understand.
- **Limitations**:
  1) Only does 1:1 renaming
  2) Only replace the tag name but not other features like attributes.

## Milestone 3
- **API**:
  ```python
  SoupReplacer(
    name_xformer=lambda tag: ...,
    attr_xformer=lambda tag: ...,
    xformer=lambda tag: ...,
  )
  ```
- **Strengths**:
  1) `name_xformer(tag) -> str` lets users express renaming logic declaratively
  and can do multiple rename by once
  (i.e. `<b>` -> `blockquote` and `<p>` -> `<div>`)
  2) `attr_xformer(tag) -> dict` allows structured attribute transforms
  (e.g. add or replace the class of all `<p>` tags to `test`)
  3) `xformer(tag)` supports arbitrary edits
  4) Enables advanced cleanup/refactoring pipelines during parsing without an
  extra tree walk.
- **Limitations**:
  1) More complex than the Milestone 2 API; users may need to understand
  Tag objects and side effects.
  2) Performance risk if heavy logic is run on every tag.

## Recommendation

I recommend keeping the simple Milestone 2 constructor
(`SoupReplacer("b", "strong")`) for straightforward tag replacements,
which is ideal for users who are new to BeautifulSoup.
For advanced use cases, the Milestone 3 functionality offers valuable
flexibility.

However, within the Milestone 3 design, I would simplify the API by keeping
only the `xformer` parameter and removing `name_xformer` and `attr_xformer`.
Functionally, `xformer` is powerful enough to perform any transformation—
renaming tags, editing attributes, or applying side effects—so the specialized
hooks are not strictly necessary. Eliminating them would make the constructor
cleaner, smaller, and easier to understand while maintaining full capability.

If future developers wish to add convenience wrappers (e.g. helpers for common
tasks like `rename_tag` or `drop_class_attr`), those can be built on top of the
single `xformer` interface rather than made into the core API.

In conclusion, the functionality introduced in Milestone 2 should be retained
for users who are new to BeautifulSoup.
For the features added in Milestone 3, we should only keep the `xformer`
parameter to maintain simplicity.