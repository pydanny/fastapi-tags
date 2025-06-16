from fastapi import FastAPI
from fastapi.testclient import TestClient
from typing import Any
import fastapi_tags as tg
from fastapi import Request


def test_TagResponse_obj():
    """Test the TagResponse class."""

    app = FastAPI()

    @app.get("/test")
    def test_endpoint():
        return tg.TagResponse(tg.H1("Hello, World!"))

    client = TestClient(app)
    response = client.get("/test")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert response.text == "<h1>Hello, World!</h1>"


def test_TagResponse_type():
    """Test the TagResponse class."""

    app = FastAPI()

    @app.get("/test", response_class=tg.TagResponse)
    def test_endpoint():
        return tg.Main(
            tg.H1("Hello, clean HTML response!"),
            tg.P("This is a paragraph in the response."),
        )

    client = TestClient(app)
    response = client.get("/test")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert (
        response.text
        == "<main><h1>Hello, clean HTML response!</h1><p>This is a paragraph in the response.</p></main>"
    )


def test_TagResponse_html():
    """Test the TagResponse class."""

    app = FastAPI()

    @app.get("/test", response_class=tg.TagResponse)
    def test_endpoint():
        return tg.Html(
            tg.Main(
                tg.H1("Hello, clean HTML response!"),
                tg.P("This is a paragraph in the response."),
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


def test_strings_and_tag_children():
    app = FastAPI()

    @app.get("/test", response_class=tg.TagResponse)
    def test_endpoint():
        return tg.Html(tg.P("This isn't a ", tg.Strong("cut off"), " sentence"))

    client = TestClient(app)
    response = client.get("/test")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert (
        response.text
        == "<!doctype html><html><p>This isn't a <strong>cut off</strong> sentence</p></html>"
    )


def test_custom_name_in_response():
    app = FastAPI()

    def Card(sentence):
        return tg.Article(tg.Header("Header"), sentence, tg.Footer("Footer"))

    @app.get("/test", response_class=tg.TagResponse)
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


def test_TagResponse_with_layout_strings():
    class CustomLayoutResponse(tg.TagResponse):
        def render(self, content: Any) -> bytes:
            content = super().render(content)
            return f"<html><body><h1>Custom Layout</h1>{content}</body></html>".encode(
                "utf-8"
            )

    app = FastAPI()

    @app.get("/test", response_class=CustomLayoutResponse)
    def test_endpoint():
        return tg.Main(tg.H2("Hello, World!"))

    client = TestClient(app)
    response = client.get("/test")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert (
        response.text
        == "<html><body><h1>Custom Layout</h1>b'<main><h2>Hello, World!</h2></main>'</body></html>"
    )


def test_TagResponse_with_layout_names():
    class CustomLayoutResponse(tg.TagResponse):
        def render(self, content: Any) -> bytes:
            content = super().render(content).decode("utf-8")
            return tg.Html(content).render().encode("utf-8")

    app = FastAPI()

    @app.get("/test", response_class=CustomLayoutResponse)
    def test_endpoint():
        return tg.Main(tg.H1("Hello, World!"))

    client = TestClient(app)
    response = client.get("/test")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert (
        response.text
        == "<!doctype html><html><main><h1>Hello, World!</h1></main></html>"
    )


def test_is_htmx():
    """Test the is_htmx method."""
    app = FastAPI()
    app.add_middleware(tg.TagHTMXMiddleware)

    @app.get("/test", response_class=tg.TagResponse)
    def test_endpoint(request: Request):
        return tg.H1("Hello, World!")

    client = TestClient(app)

    # Simulate an HTMX request by adding the hx-request header
    response = client.get("/test", headers={"hx-request": "true"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert response.headers["hx-request"] == "true"
    assert response.text == "<h1>Hello, World!</h1>"

    # Simulate a regular request by adding the hx-request header
    response = client.get("/test")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert response.headers.get("hx-request") is None
    assert response.text == "<h1>Hello, World!</h1>"
