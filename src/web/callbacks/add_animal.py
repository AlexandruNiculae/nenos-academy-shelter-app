import requests
from dash import Dash

from dash import callback_context
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output

from src.config import API_URL
from src.common.data_transfer_objects.animals import AddAnimalDto



def register_add_animal_callbacks(app: Dash) -> None:
    """
    Register add animal callbacks
    """
    @app.callback(
        Output('webapp-content', "children"),
        [
            Input("add-animal-button", "n_clicks"),
            Input("add-animal-name", "value"),
            Input("add-animal-species", "value"),
            Input("add-animal-common-name", "value"),
            Input("add-animal-rescued", "checked"),
        ]
    )
    def send_animal_info_to_api(_: int, animal_name: str, animal_species: str, animal_cname: str, animal_rescued: bool):
        trigger = callback_context.triggered[0]
        if trigger["prop_id"].split('.')[0] == "add-animal-button":
            dto = AddAnimalDto(
                name=animal_name,
                species=animal_species,
                common_name=animal_cname,
                rescued=animal_rescued,
            )
            response = requests.put(f"{API_URL}/animals", timeout=5, data=dto.json())
            return response.status_code

        raise PreventUpdate
