# FastAPI Tags

Install the package:

```bash
uv add fastapi-tags
```

Usage:

```python
from fastapi import FastAPI
import fastapi_tags as ft

app = FastAPI()

@app.get("/", response_class=FTResponse)
async def index():
    return ft.FTResponse(ft.Html(ft.H1("Hello, world!", style="color: blue;")))
```