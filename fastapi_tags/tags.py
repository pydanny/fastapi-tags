from fastcore import xml as ft
from typing import Any

from fastapi import Response


def dict_to_ft_component(d):
    children_raw = d.get("children", ())
    if isinstance(children_raw, str):
        children_raw = (children_raw,)
    # Ensure children is always a tuple
    children = tuple(
        dict_to_ft_component(c) if isinstance(c, dict) else (c,) for c in children_raw
    )
    return ft.ft(d["tag"], *children, **d.get("attrs", {}))


class FTResponse(Response):
    """Custom response class to handle Fastcore responses with fastcore FastTags."""

    media_type = "text/html; charset=utf-8"

    def render(self, content: Any) -> bytes:
        """Render the Fastcore XML element to a string."""
        if isinstance(content, dict):
            content = dict_to_ft_component(content)
        return ft.to_xml(content).encode("utf-8")
