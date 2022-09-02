from mesa import Agent
from . import Food
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
                from src.agents import Environment
                e = self.get_item(Environment)
                e.deposit_pheromone()
                self.home_move()
            else:
                self.state = FORAGING

    def home_move(self):
        from src.agents import Environment
        distances = [
            (calculate_distance(agent.pos, self.home), agent.pos)
            for agent in self.model.grid.get_neighbors(self.pos, True)
            if type(agent) is Environment
        ]
        possible_home = min(distances, key=lambda i: i[0])
        self.model.grid.move_agent(self, possible_home[1])

    def food_move(self):
        from src.agents import Environment
        possible_food = min([
            (agent.pheromone, agent.pos)
            for agent in self.model.grid.get_neighbors(self.pos, True)
            if type(agent) is Environment
        ], key=(lambda i: i[0]))

        if possible_food[0] > self.model.min_pheromone_needed:
            self.model.grid.move_agent(self, possible_food[1])
        else:
            self.random_move()

    def random_move(self):
        possible_food = self.random.choice(
            self.model.grid.get_neighborhood(self.pos, True))
        self.model.grid.move_agent(self, possible_food)
