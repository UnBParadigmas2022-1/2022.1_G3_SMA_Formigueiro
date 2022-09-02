import src.utils as utils
from mesa import Model, Agent
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid

from src.agents import ForagingAnt, Environment
from src.agents.foodAgent import Food


class Anthill(Model):
    
    def __init__(
        self,
        initial_ants,
        initial_ants_group,
        random_change_to_move,
        min_pheromone_needed,
        pheromone_deposit_rate
    ):

        self.current_id = 1
        self.width = 100
        self.height = 100

        self.schedule = SimultaneousActivation(self)
        self.grid = MultiGrid(self.width, self.height, torus=True)

        self.foods = []
        self.initial_ants = initial_ants
        self.initial_ants_group = initial_ants_group
        self.random_change_to_move = random_change_to_move / 100
        self.min_pheromone_needed = min_pheromone_needed / 10
        self.pheromone_deposit_rate = pheromone_deposit_rate / 10

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
            self.register(f)

        # Inicialização do ambiente
        for (_, x, y) in self.grid.coord_iter():
            e = Environment(self.next_id(), self, (x, y))
            self.register(e)

        food = Food(self.next_id(), self, (50, 50), 20)
        self.register(food)
        self.foods.append(food)

        self.running = True

    def step(self):
        self.schedule.step()
        self.check_empty_foods()

    def check_empty_foods(self):
        empty_foods = filter(lambda f: f.is_empty(), self.foods)

        for food in empty_foods:
            food.fill()
            self.grid.move_agent(food, utils.random_pos(self.width, self.height))

    def register(self, agent: Agent):
        self.grid.place_agent(agent, agent.pos)
        self.schedule.add(agent)
