import mesa


class ForagingAnt(mesa.Agent):
    
    def __init__(self, current_id, model, pos):
        super().__init__(current_id, model)
        self.pos = pos
