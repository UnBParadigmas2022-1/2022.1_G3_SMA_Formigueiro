from mesa import Agent

from src.agents import ForagingAnt
from src.agents.foodAgent import Food
from src.utils import get_item, random_move


class CombatentAnt(Agent):
    def __init__(self, current_id, model, pos, color):
        super().__init__(current_id, model)
        self.pos = pos
        self.home = pos
        self.color = color
        self.age = self.model.ant_max_age + self.random.randrange(100, 250)
        self.combatent_power = self.random.randrange(25, 75)

    def hurt(self, agent):
        agent.age -= self.combatent_power
        self.age += self.combatent_power

    def step(self):
        if self.age <= 0:
            food = Food(
                self.model.next_id(),
                self.model, self.pos,
                self.model.food_group
            )
            self.model.register(food)
            self.model.kill_agents.append(self)
            return

        foraging_oponent = get_item(self, ForagingAnt)
        combatent_oponent = get_item(self, CombatentAnt)

        if combatent_oponent and combatent_oponent.home != self.home:
            self.hurt(combatent_oponent)

        elif foraging_oponent and foraging_oponent.home != self.home:
            self.hurt(foraging_oponent)
        
        else:
            random_move(self)

        self.age -= 1
