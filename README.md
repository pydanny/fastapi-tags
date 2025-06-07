# FastAPI Tags

Adds fastcore fast tags to FastAPI views.

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