# FastAPI Tags

Adds s-expression HTML tags to FastAPI views. Inspired by FastHTML's use of fastcore's FT components.


<p align="center">
<a href="https://github.com/pydanny/fastapi-tags/actions?query=workflow%3Apython-package+event%3Apush+branch%main" target="_blank">
    <img src="https://github.com/pydanny/fastapi-tags/actions/workflows/python-package.yml/badge.svg?event=push&branch=main" alt="Test">
</a>
<a href="https://pypi.org/project/fastapi-tags" target="_blank">
    <img src="https://img.shields.io/pypi/v/fastapi-tags?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/fastapi-tags" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi-tags.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

## Installation:

uv:

```bash
uv add fastapi-tags
```

pip:

```bash
pip install fastapi-tags
uv pip install fastapi-tags
```


## Usage:

```python
from fastapi import FastAPI
import fastapi_tags as tg

app = FastAPI()

@app.get("/", response_class=tg.TagResponse)
async def index():
    return tg.Html(tg.H1("Hello, world!", style="color: blue;"))
```

If you want to do snippets, just skip the `tg.Html` tag:

```python
@app.get("/time", response_class=tg.TagResponse)
async def time():
    return tg.P("Time to do code!")
```

## Custom Tags

There are several ways to create custom Tags

### Subclassing

```python
class AwesomeP(tg.P) -> tg.Tag:
    def render(self) -> str:
        return f"<p{self.attrs}>AWESOME {self.children}!</p>"
AwesomeP('library')
```

```html
<p>AWESOME library!</p>
```

### Custom tags built as functions

```python
def PicoCard(header: str, body: str, footer: str) -> tg.Tag:
    return tg.Article(
        tg.Header(header),
        body,
        tg.Footer(footer)
    )
```

```python
@app.get("/card", response_class=tg.TagResponse)
async def card():
    return PicoCard(
        'FastAPI Tags',
        'Adds s-expression HTML tags (Tags) to FastAPI views.',
        'by various contributors'
    )
```

```html
<article>
    <header>FastAPI Tags</header>
    Adds s-expression HTML tags (Tags) to FastAPI views.
    <footer>by various contributors</footer>
</article>
```

## Detecting HTMX requests

The HTMX library adds a header to requests that you can use to detect HTMX requests. You can use this to return different content based on whether the request is an HTMX request or not.

```python
from fastapi import Request