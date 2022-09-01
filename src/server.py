import mesa

from src.model import Anthill
from src.agents.foragingAgent import ForagingAnt


def ant(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is ForagingAnt:
        portrayal["Color"] = ["#00FF00", "#00CC00", "#009900"]
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1
    
    return portrayal


canvas_element = mesa.visualization.CanvasGrid(ant, 100, 100, 600, 600)


model_params = {
    "initial_ants": mesa.visualization.Slider(
        "População inicial de formigas", 100, 10, 300
    ),
    "initial_ants_group": mesa.visualization.Slider(
        "Quantidade inicial de formigueiros", 2, 1, 10
    )
}


server = mesa.visualization.ModularServer(
    Anthill, [canvas_element], "Formigueiro", model_params
)
server.port = 8521
