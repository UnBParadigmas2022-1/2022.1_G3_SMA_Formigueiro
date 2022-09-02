from mesa import Agent

class Food(Agent):
    def __init__(self, current_id, model, pos):
        super().__init__(current_id, model)
        self.pos = pos

    def eat(self):
        self.model.grid.remove_agent(self)
        self.model.decrement_food()


def create_food_group(xInitial, yInitial, radius):
    for x in range(-radius, radius+1):
        for y in range(-radius, radius+1):
            if (x)**2 + (y)**2 <= radius**2:
                yield (x+xInitial, y+yInitial)