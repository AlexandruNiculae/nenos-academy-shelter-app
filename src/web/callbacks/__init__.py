from dash import Dash

from .api_status import register_api_status_callbacks
from .add_animal import register_add_animal_callbacks


def register_all_callbacks(app: Dash) -> None:
    """
    Register all component callbacks
    """
    # register_api_status_callbacks(app)
    register_add_animal_callbacks(app)
