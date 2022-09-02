from mesa import Agent

class Food(Agent):
    
    def __init__(self, current_id, model, pos, wealth):
        super().__init__(current_id, model)
        self.pos = pos
        self.wealth = wealth

    def step(self):
        self.wealth -= 1

    def random_move(self):
        possible_food = self.random.choice(
            self.model.grid.get_neighborhood(self.pos, True))
        self.model.grid.move_agent(self, possible_food)
