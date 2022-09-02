from mesa import Agent

from src.agents import Environment, Food
from src.utils import calculate_distance


FORAGING = 'PROCURANDO'
HOMING = 'VOLTANDO'


class ForagingAnt(Agent):
    
    def __init__(self, current_id, model, pos):
        super().__init__(current_id, model)
        self.state = FORAGING
        self.home = pos
        self.pos = pos

    # Retorna o agente que se encontra na posição atual
    # Baseado no exemplo sugarscape do mesa
    def get_item(self, agentType):
        for agent in self.model.grid.get_cell_list_contents([self.pos]):
            if type(agent) is agentType:
                return agent

    def step(self):
        # Procurando comida
        if self.state == FORAGING:
            food = self.get_item(Food)

            if not food:
                if self.random.random() > self.model.random_change_to_move:
                    self.food_move()
                else:
                    self.random_move()
            else:
                food.eat()
                self.state = HOMING
            
        # Voltando para casa
        elif self.state == HOMING:
            if self.pos != self.home:
                e = self.get_item(Environment)
                e.deposit_pheromone()
                self.home_move()
            else:
                self.state = FORAGING

    def home_move(self):
        possible_home = [
            (calculate_distance(agent.pos, self.home), agent.pos)
            for agent in self.model.grid.get_neighbors(self.pos, True)
            if type(agent) is Environment
        ]
        possible_home.sort(key=(lambda i: i[0]))
        if possible_home[0][1] == self.home:
            self.model.grid.move_agent(self, possible_home[0][1])
        else:
            self.model.grid.move_agent(self, possible_home[1][1])

    def food_move(self):
        possible_food = [
            (agent.pheromone, agent.pos)
            for agent in self.model.grid.get_neighbors(self.pos, True)
            if type(agent) is Environment and agent.pheromone > 0
        ]

        if not possible_food:
            self.random_move()
        else:
            possible_food = min(possible_food, key=(lambda i: i[0]))
            if possible_food[0] > self.model.min_pheromone_needed:
                self.model.grid.move_agent(self, possible_food[1])
            else:
                self.random_move()

    def random_move(self):
        possible_food = self.random.choice(
            self.model.grid.get_neighborhood(self.pos, True))
        self.model.grid.move_agent(self, possible_food)
