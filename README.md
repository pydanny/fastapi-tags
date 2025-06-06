# FastAPI Tags

Install the package:

```bash
uv add fastapi-tags
```

Usage:

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastcore import xml as ft

app = FastAPI()

@app.get("/", response_class=FTResponse)
async def index():
    return FTResponse(ft.Html(ft.H1("Hello, world!", style="color: blue;")))
```