from mesa import Agent

class Queen(Agent):
    def __init__(self, current_id, model, pos, id_anthill):
        super().__init__(current_id, model)
        self.pos = pos
        self.id_anthill = id_anthill
        

    def reproduce(self):
        self.model.create_ant(self)

