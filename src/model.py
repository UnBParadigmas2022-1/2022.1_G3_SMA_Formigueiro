import mesa


class Teste(mesa.Model):
    
    def __init__(self):
        self.grid = mesa.space.MultiGrid(100, 100, torus=True)
