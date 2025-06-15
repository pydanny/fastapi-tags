import fastapi_tags as tags


def test_atag_no_attrs_no_children():
    assert tags.A().render() == "<a></a>"


def test_atag_yes_attrs_no_children():
    tag = tags.A(href="/", cls="link").render()
    assert tag == '<a href="/" class="link"></a>'


def test_atag_yes_attrs_text_children():
    tag = tags.A("Link here", href="/", cls="link").render()
    assert tag == '<a href="/" class="link">Link here</a>'


def test_divtag_yes_attrs_a_child():
    html = tags.Div(tags.A("Link here", href="/", cls="link")).render()
    assert html == '<div><a href="/" class="link">Link here</a></div>'


def test_divtag_yes_attrs_multiple_a_children():
    html = tags.Div(
        tags.A("Link here", href="/", cls="link"),
        tags.A("Another link", href="/", cls="timid"),
    ).render()
    assert (
        html
        == '<div><a href="/" class="link">Link here</a><a href="/" class="timid">Another link</a></div>'
    )


def test_divtag_yes_attrs_nested_children():
    html = tags.Div(
        tags.P(
            "Links are here",
            tags.A("Link here", href="/", cls="link"),
            tags.A("Another link", href="/", cls="timid"),
        )
    ).render()
    assert (
        html
        == '<div><p>Links are here<a href="/" class="link">Link here</a><a href="/" class="timid">Another link</a></p></div>'
    )


def test_name_types():
    assert issubclass(tags.A, tags.Tag)
    assert issubclass(tags.Div, tags.Tag)
    assert issubclass(tags.P, tags.Tag)


def test_subclassing():
    class AwesomeP(tags.P):
        def render(self) -> str:
            return f"<p{self.attrs}>AWESOME {self.children}!</p>"

    assert AwesomeP("library").render() == "<p>AWESOME library!</p>"


def test_subclassing_nested():
    class AwesomeP(tags.P):
        def render(self) -> str:
            return f"<p{self.attrs}>AWESOME {self.children}!</p>"

    html = tags.Div(AwesomeP("library")).render()
    assert html == "<div><p>AWESOME library!</p></div>"


def test_text_child_with_sibling_elements():
    html = tags.P("This is a", tags.Strong("cut off"), "sentence").render()
    assert html == "<p>This is a<strong>cut off</strong>sentence</p>"
