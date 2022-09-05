from operator import getitem
from random import randint
from src.agents.maleAgent import Male
from src.agents.queenAgent import Queen
import src.utils as utils
from mesa import Model, Agent
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid

from src.agents import ForagingAnt, Environment, FoodGroup
from src.agents import ForagingAnt, Environment
from src.agents.combatentAgent import CombatentAnt


class Anthill(Model):

    def __init__(
        self,
        initial_ants,
        initial_ants_male,
        initial_ants_group,
        ant_max_age,
        ant_age_gain,
        random_change_to_move,
        min_pheromone_needed,
        pheromone_deposit_rate,
        food_radius,
        food_smell_distance,
        combatent_ant_qtd
    ):

        self.current_id = 1
        self.width = 100
        self.height = 100

        self.schedule = SimultaneousActivation(self)
        self.grid = MultiGrid(self.width, self.height, torus=True)

        self.initial_ants = initial_ants
        self.initial_ants_male = initial_ants_male
        self.initial_ants_group = initial_ants_group
        self.ant_age_gain = ant_age_gain
        self.ant_max_age = ant_max_age * 25
        self.random_change_to_move = random_change_to_move / 100
        self.min_pheromone_needed = min_pheromone_needed / 10
        self.pheromone_deposit_rate = pheromone_deposit_rate / 10
        self.food_smell_distance = food_smell_distance / 10
        self.food_radius = food_radius
        self.kill_agents = []
        self.combatent_ant_qtd = combatent_ant_qtd

        # Inicialização dos formigueiros
        self.groups = []
        for group in range(self.initial_ants_group):
            self.groups.append((
                self.random.randrange(self.width),
                self.random.randrange(self.height),
                [self.random.randint(0, 125) for _ in range(3)]
            ))

        # Inicialização das formigas operárias
        for ant in range(self.initial_ants):
            x, y, color = self.groups[ant % self.initial_ants_group]
            f = ForagingAnt(self.next_id(), self, (x, y), color)
            self.register(f)

        # Inicialização da rainha
        for ant in range(self.initial_ants_group):
            x, y, _ = self.groups[ant % self.initial_ants_group]
            q = Queen(self.next_id(), self, (x, y))
            self.register(q)

        # Inicialização da formiga macho
        for ant in range(self.initial_ants_male):
            x, y, _ = self.groups[ant % self.initial_ants_group]
            m = Male(self.next_id(), self, utils.random_pos(self.width, self.height), -1)
            self.register(m)

        # Inicialização das formigas combatentes
        for combatent_ant in range(self.combatent_ant_qtd):
            x, y, color = self.groups[combatent_ant % self.initial_ants_group]
            new_color = [i + 50 for i in color]
            c = CombatentAnt(self.next_id(), self, (x, y), new_color)
            self.register(c)

        # Inicialização do ambiente
        for (_, x, y) in self.grid.coord_iter():
            e = Environment(self.next_id(), self, (x, y))
            self.register(e)

        # Inicialização da comida
        self.food_group = FoodGroup(self.next_id(), self, self.food_radius)
        self.register(self.food_group)

        self.running = True

    def step(self):
        self.schedule.step()
        for x in self.kill_agents:
            self.grid.remove_agent(x)
            self.schedule.remove(x)
        self.kill_agents = []

    def create_ant(self, agent):
        radius = randint(1, 10)
        xInitial = agent.pos[0]-radius
        yInitial = agent.pos[1]-radius
        possible_create_ant = utils.random_create_ant()
        queen_group_color = utils.get_group_color(self.groups, (agent.pos[0], agent.pos[1]))
        if possible_create_ant < 30:
            new_ant = Male(self.next_id(), self, (xInitial, yInitial), agent.home)
        elif possible_create_ant >= 30  and possible_create_ant < 90:
            new_ant = ForagingAnt(self.next_id(), self, (xInitial, yInitial), queen_group_color)
        else:
            combatent_color = [i + 50 for i in queen_group_color]
            new_ant = CombatentAnt(self.next_id(), self, (xInitial, yInitial), combatent_color)
        self.register(new_ant)

    def register(self, agent: Agent):
        self.grid.place_agent(agent, agent.pos)
        self.schedule.add(agent)
