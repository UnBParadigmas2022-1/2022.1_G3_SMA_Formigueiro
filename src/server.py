import mesa

from .model import Teste


def formigueiro(agent):
    pass


canvas_element = mesa.visualization.CanvasGrid(formigueiro, 100, 100, 600, 600)


model_params = {}


server = mesa.visualization.ModularServer(
    Teste, [canvas_element], "Formigueiro", model_params
)
server.port = 8521
