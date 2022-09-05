from mesa import Agent
from src.agents.queenAgent import Queen


class Male(Agent):
    def __init__(self, current_id, model, pos, origin):
        super().__init__(current_id, model)
        self.pos = pos
        self.find_queen = False
        self.origin = origin

    def step(self):
        for neighbor in self.model.grid.get_neighborhood(self.pos):
            if type(neighbor) is Queen and neighbor.home != self.origin:
                neighbor.reproduce()
                self.find_queen = True
                self.model.kill_agents.append(self)
        if not self.find_queen:
            self.move()

    def move(self):
        possible_steps = self.random.choice(self.model.grid.get_neighborhood(self.pos, True))
        self.model.grid.move_agent(self, possible_steps)
