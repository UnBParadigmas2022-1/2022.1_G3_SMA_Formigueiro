import mesa

from src.model import Anthill
from src.render import render


canvas_element = mesa.visualization.CanvasGrid(render, 100, 100, 600, 600)


model_params = {
    "initial_ants": mesa.visualization.Slider(
        "População inicial de formigas", 100, 10, 300
    ),
    "initial_ants_male": mesa.visualization.Slider(
        "População inicial de formigas macho", 2, 1, 10
    ),
    "initial_ants_group": mesa.visualization.Slider(
        "Quantidade inicial de formigueiros", 2, 1, 10
    ),
    "random_change_to_move": mesa.visualization.Slider(
        "Possibilidade de realizar movimento aleatório", 20, 0, 100
    ),
    "min_pheromone_needed": mesa.visualization.Slider(
        "Quantidade mínima de feromônio para movimentação", 2, 0, 20
    ),
    "pheromone_deposit_rate": mesa.visualization.Slider(
        "Quantidade depositada de feromônio", 6, 0, 10
    ),
    "ant_max_age": mesa.visualization.Slider(
        "Idade máxima inicial da formiga", 5, 3, 15
    ),
    "ant_age_gain": mesa.visualization.Slider(
        "Porcentagem de vida da formiga ganha com comida", 50, 1, 100
    ),
    "food_radius": mesa.visualization.Slider(
        "Raio da comida", 15, 1, 30
    ),
    "food_smell_distance": mesa.visualization.Slider(
        "Distância do cheiro da comida", 5, 0, 10
    ),
    "combatent_ant_qtd": mesa.visualization.Slider(
        "Quantidade inicial de combatentes", 5, 1, 50
    ),
}


server = mesa.visualization.ModularServer(
    Anthill, [canvas_element], "Formigueiro", model_params
)
server.port = 8521
