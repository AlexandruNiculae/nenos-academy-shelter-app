import dash_mantine_components as dmc

from web.components.base import DashAppBaseComponent


class AddAnimalComponent(DashAppBaseComponent):

    def __init__(self):
        pass

    def render(self):
        return dmc.Stack(
            children=[
                dmc.TextInput(
                    id="add-animal-name",
                    label="Animal Name:",
                    w=200
                ),
                dmc.TextInput(
                    id="add-animal-species",
                    label="Animal Species:",
                    w=200
                ),
                dmc.TextInput(
                    id="add-animal-common-name",
                    label="Common name:",
                    w=200
                ),
                dmc.Checkbox(
                    id="add-animal-rescued",
                    label="Was the animal rescued?",
                    mb=10
                ),
                dmc.Button(
                    id="add-animal-button",
                    children="Add animal",
                    w=200,
                ),
            ],
        )
