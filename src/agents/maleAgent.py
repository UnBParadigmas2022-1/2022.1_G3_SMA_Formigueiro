from mesa import Agent
from src.agents.foodAgent import Food
from src.agents.queenAgent import Queen

from src.utils import random_move


class Male(Agent):
    def __init__(self, current_id, model, pos, origin):
        super().__init__(current_id, model)
        self.pos = pos
        self.find_queen = False
        self.origin = origin
        self.age = self.model.ant_max_age + self.random.randrange(75, 200)

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

        for neighbor in self.model.grid.get_neighborhood(self.pos, True):
            if type(neighbor) is Queen and neighbor.home != self.origin:
                neighbor.reproduce()
                self.find_queen = True
                self.model.kill_agents.append(self)
        if not self.find_queen:
            random_move(self)
