from mesa import Agent
from src.agents import ForagingAnt, Environment, Food
from functools import singledispatch
from src.agents.maleAgent import Male

from src.agents.queenAgent import Queen


@singledispatch
def render(agent: Agent):
    return


@render.register(ForagingAnt)
def foraging(agent: ForagingAnt):
    if agent.age > 0:
        return {
            "Color": '#%02x%02x%02x' % tuple(agent.color),
            "Shape": "rect",
            "Filled": "true",
            "Layer": 2,
            "w": 1,
            "h": 1
        }

@render.register(Environment)
def environment(agent: Environment):
    if agent.pheromone > 0:
        gradient = min(int(255 * agent.pheromone), 255)
        return {
            "Color": '#FF%02x%02x' % (255 - gradient, 255 - gradient),
            "Shape": "rect",
            "Filled": "true",
            "Layer": 0,
            "w": 1,
            "h": 1
        }

    gradient = min(int(125 * agent.food_smell), 255)
    return {
        "Color": '#%02xFF%02x' % (255 - gradient, 255 - gradient),
        "Shape": "rect",
        "Filled": "true",
        "Layer": 0,
        "w": 1,
        "h": 1
    }

@render.register(Food)
def food(agent: Food):
    return {
        "Color": "#00ff00",
        "Shape": "rect",
        "Filled": "true",
        "Layer": 1,
        "w": 1,
        "h": 1
    }

@render.register(Queen)
def queen(agent: Queen):
    return {
        "Color": "#f7fb4b",
        "Shape": "rect",
        "Filled": "true",
        "Layer": 2,
        "w": 2,
        "h": 2
    }

@render.register(Male)
def queen(agent: Male):
    return {
        "Color": "#0086ff",
        "Shape": "rect",
        "Filled": "true",
        "Layer": 2,
        "w": 1,
        "h": 1
    }