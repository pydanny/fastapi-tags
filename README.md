# FastAPI Tags

Usage:

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastcore import xml as ft

app = FastAPI()

@app.get("/", response_class=FTResponse)
async def index():
    return FTResponse(ft.Html(ft.H1("About Feldroy", style="color: blue;")))
```