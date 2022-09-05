from math import sqrt
from random import randint

def calculate_distance(pos1, pos2):
    return sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def random_pos(width, height):
    return (
        randint(0, width-1),
        randint(0, height-1)
    )

def random_create_ant():
    return randint(0, 100)

# Retorna o agente que se encontra na posição atual
# Baseado no exemplo sugarscape do mesa
def get_item(self, agent_type):
    for agent in self.model.grid.get_cell_list_contents([self.pos]):
        if type(agent) is agent_type and agent != self:
            return agent
