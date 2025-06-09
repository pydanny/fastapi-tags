import fastapi_tags as ft


def test_atag_no_attrs_no_children():
    assert ft.A().render() == "<a></a>\n"


def test_atag_yes_attrs_no_children():
    tag = ft.A(href="/", cls="link").render()
    assert tag == '<a href="/" class="link"></a>\n'


def test_atag_yes_attrs_text_children():
    tag = ft.A("Link here", href="/", cls="link").render()
    assert tag == '<a href="/" class="link">Link here</a>\n'


def test_divtag_yes_attrs_a_child():
    html = ft.Div(ft.A("Link here", href="/", cls="link")).render()
    assert html == '<div><a href="/" class="link">Link here</a>\n</div>\n'


def test_divtag_yes_attrs_multiple_a_children():
    html = ft.Div(
        ft.A("Link here", href="/", cls="link"),
        ft.A("Another link", href="/", cls="timid"),
    ).render()
    assert (
        html
        == '<div><a href="/" class="link">Link here</a>\n<a href="/" class="timid">Another link</a>\n</div>\n'
    )


def test_divtag_yes_attrs_nested_children():
    html = ft.Div(
        ft.P(
            "Links are here",
            ft.A("Link here", href="/", cls="link"),
            ft.A("Another link", href="/", cls="timid"),
        )
    ).render()
    assert (
        html
        == '<div><p>Links are here<a href="/" class="link">Link here</a>\n<a href="/" class="timid">Another link</a>\n</p>\n</div>\n'
    )


def test_tag_types():
    assert issubclass(ft.A, ft.FTag)
    assert issubclass(ft.Div, ft.FTag)
    assert issubclass(ft.P, ft.FTag)
