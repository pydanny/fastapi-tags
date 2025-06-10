from functools import cached_property


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
        """Sets three attributes, tag, children, and attrs.
        These are important for Starlette view responses, as nested objects
        get auto-serialized to JSON and need to be rebuilt. Without
        the values of these attributes, the object reconstruction can't occur"""
        self._tag = self.__class__.__name__
        self._module = self.__class__.__module__
        self._children, self._attrs = children, kwargs

    @property
    def tag(self) -> str:
        return self._tag.lower()

    @property
    def attrs(self) -> str:
        if not self._attrs:
            return ""
        return " " + " ".join(f'{attrmap(k)}="{v}"' for k, v in self._attrs.items())

    @cached_property
    def children(self):
        if isinstance(self._children, str | FTag):
            return self._children
        elif len(self._children) and isinstance(self._children[0], tuple):
            # TODO: If we don't force a tuple in core.FTResponse, check if this is necessary
            return "".join(
                [c.render() if isinstance(c, FTag) else c for c in self._children[0]]
            )
        return "".join(
            [c.render() if isinstance(c, FTag) else c for c in self._children]
        )

    def render(self) -> str:
        return f"<{self.tag}{self.attrs}>{self.children}</{self.tag}>"


# Special tags


class Html(FTag):
    """Defines the root of an HTML document"""

    def render(self) -> str:
        return f"<!doctype html><html{self.attrs}>{self.children}</html>"


# Stock tags


class A(FTag):
    """Defines a hyperlink"""

    pass


class Abbr(FTag):
    """Defines an abbreviation or an acronym"""

    pass


class Address(FTag):
    """Defines contact information for the author/owner of a document"""

    pass


class Area(FTag):
    """Defines an area inside an image map"""

    pass


class Article(FTag):
    """Defines an article"""

    pass


class Aside(FTag):
    """Defines content aside from the page content"""

    pass


class Audio(FTag):
    """Defines embedded sound content"""

    pass


class B(FTag):
    """Defines bold text"""

    pass


class Base(FTag):
    """Specifies the base URL/target for all relative URLs in a document"""

    pass


class Bdi(FTag):
    """Isolates a part of text that might be formatted in a different direction from other text outside it"""

    pass


class Bdo(FTag):
    """Overrides the current text direction"""

    pass


class Blockquote(FTag):
    """Defines a section that is quoted from another source"""

    pass


class Body(FTag):
    """Defines the document's body"""

    pass


class Br(FTag):
    """Defines a single line break"""

    pass


class Button(FTag):
    """Defines a clickable button"""

    pass


class Canvas(FTag):
    """Used to draw graphics, on the fly, via scripting (usually JavaScript)"""

    pass


class Caption(FTag):
    """Defines a table caption"""

    pass


class Cite(FTag):
    """Defines the title of a work"""

    pass


class Code(FTag):
    """Defines a piece of computer code"""

    pass


class Col(FTag):
    """Specifies column properties for each column within a <colgroup> element"""

    pass


class Colgroup(FTag):
    """Specifies a group of one or more columns in a table for formatting"""

    pass


class Data(FTag):
    """Adds a machine-readable translation of a given content"""

    pass


class Datalist(FTag):
    """Specifies a list of pre-defined options for input controls"""

    pass


class Dd(FTag):
    """Defines a description/value of a term in a description list"""

    pass


class Del(FTag):
    """Defines text that has been deleted from a document"""

    pass


class Details(FTag):
    """Defines additional details that the user can view or hide"""

    pass


class Dfn(FTag):
    """Specifies a term that is going to be defined within the content"""

    pass


class Dialog(FTag):
    """Defines a dialog box or window"""

    pass


class Div(FTag):
    """Defines a section in a document"""

    pass


class Dl(FTag):
    """Defines a description list"""

    pass


class Dt(FTag):
    """Defines a term/name in a description list"""

    pass


class Em(FTag):
    """Defines emphasized text"""

    pass


class Embed(FTag):
    """Defines a container for an external application"""

    pass


class Fieldset(FTag):
    """Groups related elements in a form"""

    pass


class Figcaption(FTag):
    """Defines a caption for a <figure> element"""

    pass


class Figure(FTag):
    """Specifies self-contained content"""

    pass


class Footer(FTag):
    """Defines a footer for a document or section"""

    pass


class Form(FTag):
    """Defines an HTML form for user input"""

    pass


class H1(FTag):
    """H1 header"""

    pass


class H2(FTag):
    """H2 header"""

    pass


class H3(FTag):
    """H3 header"""

    pass


class H4(FTag):
    """H4 header"""

    pass


class H5(FTag):
    """H5 header"""

    pass


class H6(FTag):
    """H6 header"""

    pass


class Head(FTag):
    """Contains metadata/information for the document"""

    pass


class Header(FTag):
    """Defines a header for a document or section"""

    pass


class Hgroup(FTag):
    """Defines a header and related content"""

    pass


class Hr(FTag):
    """Defines a thematic change in the content"""

    pass


class I(FTag):  # noqa: E742
    """Defines a part of text in an alternate voice or mood"""

    pass


class Iframe(FTag):
    """Defines an inline frame"""

    pass


class Img(FTag):
    """Defines an image"""

    pass


class Input(FTag):
    """Defines an input control"""

    pass


class Ins(FTag):
    """Defines a text that has been inserted into a document"""

    pass


class Kbd(FTag):
    """Defines keyboard input"""

    pass


class Label(FTag):
    """Defines a label for an <input> element"""

    pass


class Legend(FTag):
    """Defines a caption for a <fieldset> element"""

    pass


class Li(FTag):
    """Defines a list item"""

    pass


class Link(FTag):
    """Defines the relationship between a document and an external resource (most used to link to style sheets)"""

    pass


class Main(FTag):
    """Specifies the main content of a document"""

    pass


class Map(FTag):
    """Defines an image map"""

    pass


class Mark(FTag):
    """Defines marked/highlighted text"""

    pass


class Menu(FTag):
    """Defines an unordered list"""

    pass


class Meta(FTag):
    """Defines metadata about an HTML document"""

    pass


class Meter(FTag):
    """Defines a scalar measurement within a known range (a gauge)"""

    pass


class Nav(FTag):
    """Defines navigation links"""

    pass


class Noscript(FTag):
    """Defines an alternate content for users that do not support client-side scripts"""

    pass


class Object(FTag):
    """Defines a container for an external application"""

    pass


class Ol(FTag):
    """Defines an ordered list"""

    pass


class Optgroup(FTag):
    """Defines a group of related options in a drop-down list"""

    pass


class Option(FTag):
    """Defines an option in a drop-down list"""

    pass


class Output(FTag):
    """Defines the result of a calculation"""

    pass


class P(FTag):
    """Defines a paragraph"""

    pass


class Param(FTag):
    """Defines a parameter for an object"""

    pass


class Picture(FTag):
    """Defines a container for multiple image resources"""

    pass


class Pre(FTag):
    """Defines preformatted text"""

    pass


class Progress(FTag):
    """Represents the progress of a task"""

    pass


class Q(FTag):
    """Defines a short quotation"""

    pass


class Rp(FTag):
    """Defines what to show in browsers that do not support ruby annotations"""

    pass


class Rt(FTag):
    """Defines an explanation/pronunciation of characters (for East Asian typography)"""

    pass


class Ruby(FTag):
    """Defines a ruby annotation (for East Asian typography)"""

    pass


class S(FTag):
    """Defines text that is no longer correct"""

    pass


class Samp(FTag):
    """Defines sample output from a computer program"""

    pass


class Script(FTag):
    """Defines a client-side script"""

    pass


class Search(FTag):
    """Defines a search section"""

    pass


class Section(FTag):
    """Defines a section in a document"""

    pass


class Select(FTag):
    """Defines a drop-down list"""

    pass


class Small(FTag):
    """Defines smaller text"""

    pass


class Source(FTag):
    """Defines multiple media resources for media elements (<video> and <audio>)"""

    pass


class Span(FTag):
    """Defines a section in a document"""

    pass


class Strong(FTag):
    """Defines important text"""

    pass


class Style(FTag):
    """Defines style information for a document"""

    pass


class Sub(FTag):
    """Defines subscripted text"""

    pass


class Summary(FTag):
    """Defines a visible heading for a <details> element"""

    pass


class Sup(FTag):
    """Defines superscripted text"""

    pass


class Svg(FTag):
    """Defines a container for SVG graphics"""

    pass


class Table(FTag):
    """Defines a table"""

    pass


class Tbody(FTag):
    """Groups the body content in a table"""

    pass


class Td(FTag):
    """Defines a cell in a table"""

    pass


class Template(FTag):
    """Defines a container for content that should be hidden when the page loads"""

    pass


class Textarea(FTag):
    """Defines a multiline input control (text area)"""

    pass


class Tfoot(FTag):
    """Groups the footer content in a table"""

    pass


class Th(FTag):
    """Defines a header cell in a table"""

    pass


class Thead(FTag):
    """Groups the header content in a table"""

    pass


class Time(FTag):
    """Defines a specific time (or datetime)"""

    pass


class Title(FTag):
    """Defines a title for the document"""

    pass


class Tr(FTag):
    """Defines a row in a table"""

    pass


class Track(FTag):
    """Defines text tracks for media elements (<video> and <audio>)"""

    pass


class U(FTag):
    """Defines some text that is unarticulated and styled differently from normal text"""

    pass


class Ul(FTag):
    """Defines an unordered list"""

    pass


class Var(FTag):
    """Defines a variable"""

    pass


class Video(FTag):
    """Defines embedded video content"""

    pass


class Wbr(FTag):
    """Defines a possible line-break"""

    pass
