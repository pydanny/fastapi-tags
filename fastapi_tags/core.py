import importlib
from typing import Any
from fastapi import Response
from fastapi_tags.tags import FTag

def dict_to_ft_component(d):
    children_raw = d.get("_children", ())
    if isinstance(children_raw, str):
        children_raw = (children_raw,)
    children = tuple(
        dict_to_ft_component(c) if isinstance(c, dict) else c for c in children_raw
    )
    # TODO: cache this somehow
    module = importlib.import_module(d["_module"])
    obj = getattr(module, d["_tag"])
    return obj(*children, **d.get("_attrs", {}))


class FTResponse(Response):
    """Custom response class to handle FTags."""

    media_type = "text/html; charset=utf-8"

    def render(self, content: Any) -> bytes:
        """Render FTag elements to bytes of HTML."""
        if isinstance(content, dict):
            content = dict_to_ft_component(content)
        return content.render().encode("utf-8")
