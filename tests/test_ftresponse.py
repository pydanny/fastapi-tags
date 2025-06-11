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
    assert response.text == "<h1>Hello, World!</h1>"


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
        == "<main><h1>Hello, clean HTML response!</h1><p>This is a paragraph in the response.</p></main>"
    )


def test_ftresponse_html():
    """Test the FTResponse class."""
    import fastapi_tags as ft

    app = FastAPI()

    @app.get("/test", response_class=ft.FTResponse)
    def test_endpoint():
        return ft.Html(
            ft.Main(
                ft.H1("Hello, clean HTML response!"),
                ft.P("This is a paragraph in the response."),
            )
        )

    client = TestClient(app)
    response = client.get("/test")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert (
        response.text
        == "<!doctype html><html><main><h1>Hello, clean HTML response!</h1><p>This is a paragraph in the response.</p></main></html>"
    )


def test_strings_and_ft_children():
    import fastapi_tags as ft

    app = FastAPI()

    @app.get("/test", response_class=ft.FTResponse)
    def test_endpoint():
        return ft.Html(ft.P("This isn't a ", ft.Strong("cut off"), " sentence"))

    client = TestClient(app)
    response = client.get("/test")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert (
        response.text
        == "<!doctype html><html><p>This isn't a <strong>cut off</strong> sentence</p></html>"
    )


def test_custom_ftag_in_response():
    import fastapi_tags as ft

    app = FastAPI()

    def Card(sentence):
        return ft.Article(ft.Header("Header"), sentence, ft.Footer("Footer"))

    @app.get("/test", response_class=ft.FTResponse)
    def test_endpoint():
        return Card("This is a sentence")

    client = TestClient(app)
    response = client.get("/test")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert (
        response.text
        == "<article><header>Header</header>This is a sentence<footer>Footer</footer></article>"
    )
