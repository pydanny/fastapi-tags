def _fix_k(k):
    # This function originated in fastcore.
    return k if k == "_" else k.lstrip("_").replace("_", "-")


_specials = set("@.-!~:[](){}$%^&*+=|/?<>,`")


def attrmap(o):
    """Converts shims for class and for such as _class, cls, _for, fr into
    their HTML implementations
    """
    # This function originated in fastcore.
    if _specials & set(o):
        return o
    o = dict(
        htmlClass="class",
        cls="class",
        _class="class",
        klass="class",
        _for="for",
        fr="for",
        htmlFor="for",
    ).get(o, o)
    return _fix_k(o)


class FTag:
    def __init__(self, *children, **kwargs):
        self.children, self.attrs = children, kwargs

    def _stringify_attrs(self) -> str:
        if not self.attrs:
            return ""
        return " " + " ".join(f'{attrmap(k)}="{v}"' for k, v in self.attrs.items())

    def render(self) -> str:
        tag = self.__class__.__name__.lower()
        if isinstance(self.children, str):
            children = self.children
        else:
            children = "".join(
                [c.render() if isinstance(c, FTag) else c for c in self.children]
            )
        return f"<{tag}{self._stringify_attrs()}>{children}</{tag}>"


class A(FTag):
    pass


class Article(FTag):
    pass


class Aside(FTag):
    pass


class Audio(FTag):
    pass


class B(FTag):
    pass


class Block(FTag):
    pass


class Body(FTag):
    pass


class Br(FTag):
    pass


class Button(FTag):
    pass


class Canvas(FTag):
    pass


class Caption(FTag):
    pass


class Code(FTag):
    pass


class Col(FTag):
    pass


class Colgroup(FTag):
    pass


class Dd(FTag):
    pass


class Details(FTag):
    pass


class Div(FTag):
    pass


class Dl(FTag):
    pass


class Dt(FTag):
    pass


class Em(FTag):
    pass


class Embed(FTag):
    pass


class Fieldset(FTag):
    pass


class Figcaption(FTag):
    pass


class Figure(FTag):
    pass


class Footer(FTag):
    pass


class Form(FTag):
    pass


class H1(FTag):
    pass


class H2(FTag):
    pass


class H3(FTag):
    pass


class H4(FTag):
    pass


class H5(FTag):
    pass


class H6(FTag):
    pass


class Head(FTag):
    pass


class Header(FTag):
    pass


class Hr(FTag):
    pass


class Html(FTag):
    pass


class I(FTag):  # noqa: E742
    pass


class Iframe(FTag):
    pass


class Img(FTag):
    pass


class Input(FTag):
    pass


class Label(FTag):
    pass


class Legend(FTag):
    pass


class Li(FTag):
    pass


class Link(FTag):
    pass


class Main(FTag):
    pass


class Mark(FTag):
    pass


class Math(FTag):
    pass


class Meta(FTag):
    pass


class Nav(FTag):
    pass


class Noscript(FTag):
    pass


class Object(FTag):
    pass


class Ol(FTag):
    pass


class Option(FTag):
    pass


class P(FTag):
    pass


class Param(FTag):
    pass


class Pre(FTag):
    pass


class S(FTag):
    pass


class Script(FTag):
    pass


class Section(FTag):
    pass


class Select(FTag):
    pass


class Slot(FTag):
    pass


class Small(FTag):
    pass


class Source(FTag):
    pass


class Span(FTag):
    pass


class Strike(FTag):
    pass


class Strong(FTag):
    pass


class Style(FTag):
    pass


class Sub(FTag):
    pass


class Summary(FTag):
    pass


class Sup(FTag):
    pass


class Svg(FTag):
    pass


class Table(FTag):
    pass


class Tbody(FTag):
    pass


class Td(FTag):
    pass


class Template(FTag):
    pass


class Textarea(FTag):
    pass


class Tfoot(FTag):
    pass


class Th(FTag):
    pass


class Thead(FTag):
    pass


class Title(FTag):
    pass


class Tr(FTag):
    pass


class U(FTag):
    pass


class Ul(FTag):
    pass


class Video(FTag):
    pass
