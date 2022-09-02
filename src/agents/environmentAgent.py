from mesa import Agent


class Environment(Agent):
    
    def __init__(self, current_id, model, pos):
        super().__init__(current_id, model)
        self.pheromone = 0.0
        self.pos = pos

    def step(self):
        if self.pheromone > 0:
            self.pheromone -= 0.01

    def deposit_pheromone(self):
        if self.pheromone < 1:
            self.pheromone = min(
                self.pheromone + self.model.pheromone_deposit_rate, 1)
