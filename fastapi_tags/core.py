import importlib
from typing import Any
from fastapi import Response, Header


def is_htmx_request(hx_request: str = Header(default=None)) -> bool:
    return hx_request is not None and hx_request.lower() == "true"


def dict_to_ft_component(d):
    children_raw = d.get("_children", ())
    children = tuple(
        dict_to_ft_component(c) if isinstance(c, dict) else c for c in children_raw
    )
    module = importlib.import_module(d["_module"])
    obj = getattr(module, d["_name"])
    return obj(*children, **d.get("_attrs", {}))


class TagResponse(Response):
    """Custom response class to handle fastapi_tags.tags.Tags."""

    media_type = "text/html; charset=utf-8"

    def render(self, content: Any) -> bytes:
        """Render Tag elements to bytes of HTML."""
        if isinstance(content, dict):
            content = dict_to_ft_component(content)
        return content.render().encode("utf-8")
