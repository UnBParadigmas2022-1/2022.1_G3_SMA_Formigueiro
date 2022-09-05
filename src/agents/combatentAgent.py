from mesa import Agent

from src.agents import ForagingAnt
from src.agents.foodAgent import Food
from src.utils import get_item


class CombatentAnt(Agent):
    def __init__(self, current_id, model, pos, color):
        super().__init__(current_id, model)
        self.pos = pos
        self.home = pos
        self.color = color
        self.decomposing = True
        self.age = self.model.ant_max_age + self.random.randrange(100, 250)
        self.combatent_power = self.random.randrange(25, 50)

    def hurt(self, agent):
        agent.age -= self.combatent_power

    def step(self):
        if self.age <= 0:
            if self.decomposing:
                self.decomposing = False
                food = Food(
                    self.model.next_id(),
                    self.model, self.pos,
                    self.model.food_group
                )
                self.model.register(food)
            return

        foraging_oponent = get_item(self, ForagingAnt)
        combatent_oponent = get_item(self, CombatentAnt)

        if combatent_oponent and combatent_oponent.home != self.home:
            self.hurt(combatent_oponent)

        elif foraging_oponent and foraging_oponent.home != self.home:
            self.hurt(foraging_oponent)
        
        else:
            self.random_move()

        self.age -= 1
    
    # Movimento aleatório
    def random_move(self):
        possible_food = self.random.choice(
            self.model.grid.get_neighborhood(self.pos, True))
        self.model.grid.move_agent(self, possible_food)
