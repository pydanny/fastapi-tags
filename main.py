import fastapi_tags as ft
from fastapi import FastAPI
import uvicorn

app = FastAPI()


class AwesomeP(ft.P):
    def render(self) -> str:
        return f"<p{self.attrs}>AWESOME {self.children}!</p>"


@app.get("/", response_class=ft.FTResponse)
def home():
    """EidosUI MVP showcase"""
    return layout(
        ft.P("Regular P"),
        AwesomeP("AWESOME P"),
        ft.P("This is a ", ft.Strong("cut off"), " sentence").render(),
    )


def layout(*content):
    return ft.Html(
        ft.Head(
            ft.Title("Custom Component"),
        ),
        ft.Body(
            *content,
        ),
    )


if __name__ == "__main__":
    uvicorn.run("custom_componet:app", host="0.0.0.0", port=8000, reload=True)
