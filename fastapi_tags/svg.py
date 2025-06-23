from .tags import Tag


class SvgTag(Tag):
    @property
    def name(self) -> str:
        if not self._name:
            return self._name
        return self._name[0].lower() + self._name[1:]


class A(SvgTag):
    pass


class Animate(SvgTag):
    pass


class AnimateMotion(SvgTag):
    pass


class AnimateTransform(SvgTag):
    pass


class Circle(SvgTag):
    pass


class ClipPath(SvgTag):
    pass


class Defs(SvgTag):
    pass


class Desc(SvgTag):
    pass


class Ellipse(SvgTag):
    pass


class FeBlend(SvgTag):
    pass


class FeColorMatrix(SvgTag):
    pass


class FeComponentTransfer(SvgTag):
    pass


class FeComposite(SvgTag):
    pass


class FeConvolveMatrix(SvgTag):
    pass


class FeDiffuseLighting(SvgTag):
    pass


class FeDisplacementMap(SvgTag):
    pass


class FeDistantLight(SvgTag):
    pass


class FeDropShadow(SvgTag):
    pass


class FeFlood(SvgTag):
    pass


class FeFuncA(SvgTag):
    pass


class FeFuncB(SvgTag):
    pass


class FeFuncG(SvgTag):
    pass


class FeFuncR(SvgTag):
    pass


class FeGaussianBlur(SvgTag):
    pass


class FeImage(SvgTag):
    pass


class FeMerge(SvgTag):
    pass


class FeMergeNode(SvgTag):
    pass


class FeMorphology(SvgTag):
    pass


class FeOffset(SvgTag):
    pass


class FePointLight(SvgTag):
    pass


class FeSpecularLighting(SvgTag):
    pass


class FeSpotLight(SvgTag):
    pass


class FeTile(SvgTag):
    pass


class FeTurbulence(SvgTag):
    pass


class Filter(SvgTag):
    pass


class ForeignObject(SvgTag):
    pass


class G(SvgTag):
    pass


class Image(SvgTag):
    pass


class Line(SvgTag):
    pass


class LinearGradient(SvgTag):
    pass


class Marker(SvgTag):
    pass


class Mask(SvgTag):
    pass


class Metadata(SvgTag):
    pass


class Mpath(SvgTag):
    pass


class Path(SvgTag):
    pass


class Pattern(SvgTag):
    pass


class Polygon(SvgTag):
    pass


class Polyline(SvgTag):
    pass


class RadialGradient(SvgTag):
    pass


class Rect(SvgTag):
    pass


class Script(SvgTag):
    pass


class Set(SvgTag):
    pass


class Stop(SvgTag):
    pass


class Style(SvgTag):
    pass


class Svg(SvgTag):
    pass


class Switch(SvgTag):
    pass


class Symbol(SvgTag):
    pass


class Text(SvgTag):
    pass


class TextPath(SvgTag):
    pass


class Title(SvgTag):
    pass


class Tspan(SvgTag):
    pass


class Use(SvgTag):
    pass


class View(SvgTag):
    pass
