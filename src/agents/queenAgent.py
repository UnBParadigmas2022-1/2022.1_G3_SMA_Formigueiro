from mesa import Agent

class Queen(Agent):
    def __init__(self, current_id, model, pos):
        super().__init__(current_id, model)
        self.pos = pos
        self.home = pos

    def reproduce(self):
        self.model.create_ant(self)

