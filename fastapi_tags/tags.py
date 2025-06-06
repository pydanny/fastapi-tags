from fastcore import xml as ft
from typing import Any

from fastapi import Response

class FTResponse(Response):
    """Custom response class to handle Fastcore responses with fastcore FastTags."""

    media_type = "text/html; charset=utf-8"

    def render(self, content: Any) -> bytes:
        """Render the Fastcore XML element to a string."""
        return ft.to_xml(content).encode("utf-8")
