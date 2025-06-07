# FastAPI Tags

Adds fastcore fast tags to FastAPI views.


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

Install the package:

```bash
uv add fastapi-tags
```

Usage:

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