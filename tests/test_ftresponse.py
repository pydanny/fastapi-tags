from fastapi import FastAPI
from fastapi.testclient import TestClient


def test_ftresponse_obj():
    """Test the FTResponse class."""
    import fastapi_tags as ft

    app = FastAPI()

    @app.get("/test")
    def test_endpoint():
        return ft.FTResponse(ft.H1("Hello, World!"))

    client = TestClient(app)
    response = client.get("/test")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert response.text == "<h1>Hello, World!</h1>\n"


def test_ftresponse_type():
    """Test the FTResponse class."""
    import fastapi_tags as ft

    app = FastAPI()

    @app.get("/test", response_class=ft.FTResponse)
    def test_endpoint():
        return ft.Main(
            ft.H1("Hello, clean HTML response!"),
            ft.P("This is a paragraph in the response."),
        )

    client = TestClient(app)
    response = client.get("/test")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert (
        response.text
        == "<main>  <h1>Hello, clean HTML response!</h1>\n  <p>This is a paragraph in the response.</p>\n</main>"
    )
