from mesa import Agent


class Male(Agent):
    def __init__(self, current_id, model, pos):
        super().__init__(current_id, model)
        self.pos = pos

    def step(self):
        pass