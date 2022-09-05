from mesa import Agent


class Environment(Agent):
    
    def __init__(self, current_id, model, pos):
        super().__init__(current_id, model)
        self.pheromone = 0.0
        self.food_smell = 0.0
        self.pos = pos

    def step(self):
        if self.pheromone > 0:
            self.pheromone -= 0.01
        self.propagate_food_smell()

    def deposit_pheromone(self):
        if self.pheromone < 1:
            self.pheromone = min(
                self.pheromone + self.model.pheromone_deposit_rate, 1)

            neighbors = [
                e for e in self.model.grid.get_neighbors(self.pos, True)
                if type(e) is Environment
            ]

            self.random.shuffle(neighbors)
            for e in neighbors[:2]:
                e.pheromone = min(
                    self.pheromone + self.model.pheromone_deposit_rate, 1)

    def propagate_food_smell(self):
        from src.agents import Food
        sum_smell = 0
        for e in self.model.grid.get_neighbors(self.pos, True):
            if type(e) is Food:
                self.food_smell = self.model.food_smell_distance
                return
            elif type(e) is Environment and e.food_smell > 0.05:
                sum_smell += e.food_smell

        self.food_smell = min(sum_smell/8, self.model.food_smell_distance)
        if(self.food_smell <= 0.01):
            self.food_smell = 0
