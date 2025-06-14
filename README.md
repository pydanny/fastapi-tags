# FastAPI Tags

Adds s-expression HTML tags (FTags) to FastAPI views. Inspired by FastHTML's use of fastcore's FT components.


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


# Usage:

```python
from fastapi import FastAPI
import fastapi_tags as ft

app = FastAPI()

@app.get("/", response_class=ft.FTResponse)
async def index():
    return ft.Html(ft.H1("Hello, world!", style="color: blue;"))
```

If you want to do snippets, just skip the `ft.Html` tag:

```python
@app.get("/time", response_class=ft.FTResponse)
async def time():
    return ft.P("Time to do code!")
```

# Custom FTags

There are several ways to create custom FTags

# Subclassing

```python
class AwesomeP(ft.P) -> ft.FTag:
    def render(self) -> str:
        return f"<p{self.attrs}>AWESOME {self.children}!</p>"
AwesomeP('library')
```

```html
<p>AWESOME library!</p>
```

# Custom tags built as functions

```python
def PicoCard(header: str, body: str, footer: str) -> ft.FTag:
    return ft.Article(
        ft.Header(header),
        body,
        ft.Footer(footer)
    )
```

```python
@app.get("/card", response_class=ft.FTResponse)
async def card():
    return PicoCard(
        'FastAPI Tags',
        'Adds s-expression HTML tags (FTags) to FastAPI views.',
        'by various contributors'
    )
```

```html
<article>
    <header>FastAPI Tags</header>
    Adds s-expression HTML tags (FTags) to FastAPI views.
    <footer>by various contributors</footer>
</article>
```

# Layouts

Layouts are a way to define a common structure for your HTML pages. You can create a layout by defining it with FTags and then 

```python