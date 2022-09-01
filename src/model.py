import mesa

from src.agents.foragingAgent import ForagingAnt


class Anthill(mesa.Model):
    
    def __init__(self, initial_ants, initial_ants_group):
        self.current_id = 1
        self.width = 100
        self.height = 100

        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.Grid(self.width, self.height, torus=False)

        self.initial_ants = initial_ants
        self.initial_ants_group = initial_ants_group

        # Inicialização dos formigueiros
        groups = []
        for group in range(self.initial_ants_group):
            groups.append((
                self.random.randrange(self.width),
                self.random.randrange(self.height)
            ))

        # Inicialização das formigas operárias
        for ant in range(self.initial_ants):
            pos = groups[ant % self.initial_ants_group]
            f = ForagingAnt(self.next_id(), self, pos)
            self.grid.place_agent(f, pos)
            self.schedule.add(f)

        self.running = True
