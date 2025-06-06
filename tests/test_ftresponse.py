from fastapi import FastAPI
from fastapi.testclient import TestClient


def test_ftresponse():
    """Test the FTResponse class."""
    from fastcore import xml as ft  # type: ignore
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

