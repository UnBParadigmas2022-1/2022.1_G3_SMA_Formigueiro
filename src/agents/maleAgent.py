from random import randint
from mesa import Agent
from src.agents.environmentAgent import Environment
from src.agents.foodAgent import Food
from src.agents.queenAgent import Queen

from src.utils import calculate_distance, get_item, random_move


class Male(Agent):
    def __init__(self, current_id, model, pos, origin):
        super().__init__(current_id, model)
        self.pos = pos
        self.origin = origin
        self.age = self.model.ant_max_age + self.random.randrange(75, 200)
        self.hunting_queen = self.define_hunting_queen()

    def step(self): 
        if self.age <= 0:
            food = Food(
                self.model.next_id(),
                self.model, self.pos,
                self.model.food_group
            )
            self.model.register(food)
            self.model.kill_agents.append(self)
            return

        self.reproduction_move()

    def define_hunting_queen(self):
        if self.origin == -1:
            return (lambda g: (g[0], g[1]))(self.random.choice(self.model.groups))
        else:
            return self.random.choice(
                list(set([(x, y) for x, y, _ in self.model.groups]).difference([self.origin]))
            )

    def reproduction_move(self):
        possible_queen = [
            (calculate_distance(agent.pos, self.hunting_queen), agent.pos)
            for agent in self.model.grid.get_neighbors(self.pos, True)
            if type(agent) is Environment
        ]
        possible_queen.sort(key=(lambda i: i[0]))
        if possible_queen[0][1] == self.hunting_queen:
            self.model.grid.move_agent(self, possible_queen[0][1])
            queen = get_item(self, Queen)
            queen.reproduce()
            self.model.kill_agents.append(self)
        else:
            self.model.grid.move_agent(self, possible_queen[1][1])