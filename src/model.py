from mesa import Model, Agent
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid

from src.agents import ForagingAnt, Environment, FoodGroup


class Anthill(Model):
    
    def __init__(
        self,
        initial_ants,
        initial_ants_group,
        ant_max_age,
        ant_age_gain,
        random_change_to_move,
        min_pheromone_needed,
        pheromone_deposit_rate,
        food_radius,
        food_smell_distance,
    ):

        self.current_id = 1
        self.width = 100
        self.height = 100

        self.schedule = SimultaneousActivation(self)
        self.grid = MultiGrid(self.width, self.height, torus=True)

        self.initial_ants = initial_ants
        self.initial_ants_group = initial_ants_group
        self.ant_age_gain = ant_age_gain
        self.ant_max_age = ant_max_age * 25
        self.random_change_to_move = random_change_to_move / 100
        self.min_pheromone_needed = min_pheromone_needed / 10
        self.pheromone_deposit_rate = pheromone_deposit_rate / 10
        self.food_smell_distance = food_smell_distance / 10
        self.food_radius = food_radius

        # Inicialização dos formigueiros
        groups = []
        for group in range(self.initial_ants_group):
            groups.append((
                self.random.randrange(self.width),
                self.random.randrange(self.height),
                [self.random.randint(0, 125) for _ in range(3)]
            ))

        # Inicialização das formigas operárias
        for ant in range(self.initial_ants):
            x, y, color = groups[ant % self.initial_ants_group]
            f = ForagingAnt(self.next_id(), self, (x, y), color)
            self.register(f)

        # Inicialização do ambiente
        for (_, x, y) in self.grid.coord_iter():
            e = Environment(self.next_id(), self, (x, y))
            self.register(e)

        # Inicialização da comida
        food_group = FoodGroup(self.next_id(), self, self.food_radius)
        self.register(food_group)

        self.running = True

    def step(self):
        self.schedule.step()

    def register(self, agent: Agent):
        self.grid.place_agent(agent, agent.pos)
        self.schedule.add(agent)
