from mesa import Agent
from src.utils import random_pos

class Food(Agent):
    def __init__(self, current_id, model, pos, food_group):
        super().__init__(current_id, model)
        self.pos = pos
        self.food_group = food_group

    def eat(self):
        self.food_group.remove_food(self)


class FoodGroup(Agent):
    def __init__(self, current_id, model, radius):
        super().__init__(current_id, model)
        self.pos = (0,0)
        self.radius = radius
        self.foods = 0
        self.create_foods()

    def step(self):
        if self.foods == 0:
            self.create_foods()

    def remove_food(self, food):
        self.model.grid.remove_agent(food)
        self.foods -= 1

    def create_foods(self):
        xInitial, yInitial = random_pos(
            self.model.width-self.radius,
            self.model.height-self.radius
        )

        for food_pos in self.generate_food_positions(xInitial, yInitial):
            food = Food(self.model.next_id(), self.model, food_pos, self)
            self.model.register(food)
            self.foods += 1

    def generate_food_positions(self, xInitial, yInitial):
        in_circle = lambda x, y: (x)**2 + (y)**2 <= self.radius**2

        for x in range(-self.radius, self.radius+1):
            for y in range(-self.radius, self.radius+1):
                if in_circle(x, y):
                    yield (x+xInitial, y+yInitial)