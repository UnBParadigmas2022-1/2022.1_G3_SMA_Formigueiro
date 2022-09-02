from mesa import Agent
from random import randint

class Food(Agent):
    
    def __init__(self, current_id, model, pos, wealth):
        super().__init__(current_id, model)
        self.pos = pos
        self.wealth = wealth

    def step(self):
        self.wealth -= 1

    def is_empty(self):
        return self.wealth == 0

    def fill(self):
        self.wealth = randint(10, 100)

