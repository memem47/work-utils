"""Top-level package for work-utils."""

from importlib.metadata import PackageNotFoundError, version as _v

# ----------------------------------------------------------------------
# Dynamic version retrieval --------------------------------------------
# ----------------------------------------------------------------------
try:
    # When installed (pip install work-utils), metadata is available
    __version__: str = _v(__name__)          # type: ignore[assignment]
except PackageNotFoundError:
    # Editable or source checkout (pip install -e .)
    __version__ = "0.0.0+dev"

# ----------------------------------------------------------------------
# Public API -----------------------------------------------------------
# ----------------------------------------------------------------------
__all__ = [
    "load_image",
]

from .io import load_image                       # noqa: E402 F401
