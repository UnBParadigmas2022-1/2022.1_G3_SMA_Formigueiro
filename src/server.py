import mesa

from src.model import Anthill
from src.agents import ForagingAnt, Environment


def ant(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is ForagingAnt:
        portrayal["Color"] = "#8B4513"
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Layer"] = 1
        portrayal["w"] = 1
        portrayal["h"] = 1

    if type(agent) is Environment:
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1

        gradient = min(int(255 * agent.pheromone), 255)
        portrayal["Color"] = '#FF%02x%02x' % (255 - gradient, 255 - gradient)
    
    return portrayal


canvas_element = mesa.visualization.CanvasGrid(ant, 100, 100, 600, 600)


model_params = {
    "initial_ants": mesa.visualization.Slider(
        "População inicial de formigas", 100, 10, 300
    ),
    "initial_ants_group": mesa.visualization.Slider(
        "Quantidade inicial de formigueiros", 2, 1, 10
    ),
    "random_change_to_move": mesa.visualization.Slider(
        "Possibilidade de realizar movimento aleatório", 20, 0, 100
    ),
    "min_pheromone_needed": mesa.visualization.Slider(
        "Quantidade mínima de feromônio para movimentação", 5, 0, 20
    ),
    "pheromone_deposit_rate": mesa.visualization.Slider(
        "Quantidade depositada de feromônio", 1, 0, 10
    ),
}


server = mesa.visualization.ModularServer(
    Anthill, [canvas_element], "Formigueiro", model_params
)
server.port = 8521
