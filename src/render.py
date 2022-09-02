from mesa import Agent
from src.agents import ForagingAnt, Environment, Food
from functools import singledispatch


@singledispatch
def render(agent: Agent):
    return


@render.register(ForagingAnt)
def foraging(agent: ForagingAnt):
    return {
        "Color": "#8B4513",
        "Shape": "rect",
        "Filled": "true",
        "Layer": 1,
        "w": 1,
        "h": 1
    }

@render.register(Environment)
def environment(agent: Environment):
    gradient = min(int(255 * agent.pheromone), 255)
    return {
        "Color": '#FF%02x%02x' % (255 - gradient, 255 - gradient),
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
        "Shape": "circle",
        "Filled": "true",
        "Layer": 2,
        "r": max(agent.wealth / 5, 10),
        "text": agent.wealth,
        "text_color": "#000000"
    }