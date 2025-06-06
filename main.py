from fastcore import xml as ft  # type: ignore
from typing import Any

from fastapi import Response


class FTResponse(Response):
    """Custom response class to handle Fastcore XML responses."""

    media_type = "text/html"

    def render(self, content: Any) -> bytes:
        """Render the Fastcore XML element to a string."""
        return ft.to_xml(content)


def main():
    print("Hello from fastapi-tags!")


if __name__ == "__main__":
    main()
