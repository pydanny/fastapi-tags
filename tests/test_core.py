from fastapi import FastAPI
from fastapi.testclient import TestClient
from typing import Any


def test_nameResponse_obj():
    """Test the TagResponse class."""
    import fastapi_tags as tags

    app = FastAPI()

    @app.get("/test")
    def test_endpoint():
        return tags.TagResponse(tags.H1("Hello, World!"))

    client = TestClient(app)
    response = client.get("/test")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert response.text == "<h1>Hello, World!</h1>"


def test_nameResponse_type():
    """Test the TagResponse class."""
    import fastapi_tags as tags

    app = FastAPI()

    @app.get("/test", response_class=tags.TagResponse)
    def test_endpoint():
        return tags.Main(
            tags.H1("Hello, clean HTML response!"),
            tags.P("This is a paragraph in the response."),
        )

    client = TestClient(app)
    response = client.get("/test")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert (
        response.text
        == "<main><h1>Hello, clean HTML response!</h1><p>This is a paragraph in the response.</p></main>"
    )


def test_nameResponse_html():
    """Test the TagResponse class."""
    import fastapi_tags as tags

    app = FastAPI()

    @app.get("/test", response_class=tags.TagResponse)
    def test_endpoint():
        return tags.Html(
            tags.Main(
                tags.H1("Hello, clean HTML response!"),
                tags.P("This is a paragraph in the response."),
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
    import fastapi_tags as tags

    app = FastAPI()

    @app.get("/test", response_class=tags.TagResponse)
    def test_endpoint():
        return tags.Html(tags.P("This isn't a ", tags.Strong("cut off"), " sentence"))

    client = TestClient(app)
    response = client.get("/test")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert (
        response.text
        == "<!doctype html><html><p>This isn't a <strong>cut off</strong> sentence</p></html>"
    )


def test_custom_name_in_response():
    import fastapi_tags as tags

    app = FastAPI()

    def Card(sentence):
        return tags.Article(tags.Header("Header"), sentence, tags.Footer("Footer"))

    @app.get("/test", response_class=tags.TagResponse)
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


def test_nameResponse_with_layout_strings():
    import fastapi_tags as tags

    class CustomLayoutResponse(tags.TagResponse):
        def render(self, content: Any) -> bytes:
            content = super().render(content)
            return f"<html><body><h1>Custom Layout</h1>{content}</body></html>".encode(
                "utf-8"
            )

    app = FastAPI()

    @app.get("/test", response_class=CustomLayoutResponse)
    def test_endpoint():
        return tags.Main(tags.H2("Hello, World!"))

    client = TestClient(app)
    response = client.get("/test")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert (
        response.text
        == "<html><body><h1>Custom Layout</h1>b'<main><h2>Hello, World!</h2></main>'</body></html>"
    )


def test_nameResponse_with_layout_names():
    import fastapi_tags as tags

    class CustomLayoutResponse(tags.TagResponse):
        def render(self, content: Any) -> bytes:
            content = super().render(content).decode("utf-8")
            return tags.Html(content).render().encode("utf-8")

    app = FastAPI()

    @app.get("/test", response_class=CustomLayoutResponse)
    def test_endpoint():
        return tags.Main(tags.H1("Hello, World!"))

    client = TestClient(app)
    response = client.get("/test")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert (
        response.text
        == "<!doctype html><html><main><h1>Hello, World!</h1></main></html>"
    )
