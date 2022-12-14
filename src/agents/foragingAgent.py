from mesa import Agent

from src.agents import Environment, Food
from src.utils import calculate_distance, get_item, random_move


FORAGING = 'PROCURANDO'
HOMING = 'VOLTANDO'


class ForagingAnt(Agent):
    
    def __init__(self, current_id, model, pos, color):
        super().__init__(current_id, model)
        self.state = FORAGING
        self.home = pos
        self.pos = pos
        self.age = self.model.ant_max_age + self.random.randrange(75, 200)
        self.color = color
        self.with_food = False
        self.go_home = self.random.randrange(100, 200)

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

        food = get_item(self, Food)
        # Procurando comida
        if self.state == FORAGING:
            # Não encontrou comida
            if not food:
                self.go_home -= 1
                # Se o mãximo de exploração foi atingido, volta pra casa
                if self.go_home <= 0:
                    self.home_move()
                    self.state = HOMING
                # Randomiza e calcula a chance de seguir pelo feromônio
                elif self.random.random() > self.model.random_change_to_move:
                    self.food_move()
                # Se não, movimento aleatório
                else:
                    random_move(self)
            # Achou comida, volta pra casa com ela
            else:
                food.eat()
                self.age *= (1 + (self.model.ant_age_gain / 100))
                e = get_item(self, Environment)
                e.food_smell = 0
                self.with_food = True
                self.state = HOMING
            
        # Voltando para casa
        elif self.state == HOMING:
            # Enquanto não estiver em casa
            if self.pos != self.home:
                e = get_item(self, Environment)
                # Se estiver carregando comida, deposita feromônio
                if self.with_food:
                    e.deposit_pheromone()
                    self.home_move()
                # Se não, tiver comida e achar um caminho ou comida, faz o movimento de comida
                elif food or e.pheromone > 0 or e.food_smell:
                    self.state = FORAGING
                    self.food_move()
                # Se não, só volta pra casa
                else:
                    self.home_move()
            # Estando em casa, volta a procurar comida
            else:
                self.go_home = self.random.randrange(100, 200)
                self.with_food = False
                self.state = FORAGING

        self.age -= 1

    # Procura caminhos para voltar pra casa, para não ser ideal usa
    # o segundo melhor caminho encontrado. Se o melhor caminho for 
    # a sua casa, usa ele
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

    # Procura feromônios
    def food_move(self):
        food_smells = []
        food_points = []
        possible_food = []
        neighbors = self.model.grid.get_neighbors(self.pos, True)

        for agent in neighbors:
            # Salva se o vizinho for um ponto de comida
            if type(agent) is Food:
                food_points.append(agent.pos)
            else:
                # Se não, só salva se tiver feromônio
                if type(agent) is Environment and agent.pheromone > 0:
                    possible_food.append((agent.pheromone, agent.pos))
                # Se não, só salva se tiver cheiro de comida
                if type(agent) is Environment and agent.food_smell > 0:
                    food_smells.append((agent.food_smell, agent.pos))

        # Se tiver encontrado comida, randomiza e usa um desses pontos
        if food_points:
            self.model.grid.move_agent(self, food_points[0])
        # Se não tiver encontrado nem comida, nem feromônio e nem cheiro movimenta aleatoriamente
        elif not possible_food and not food_smells:
            random_move(self)
        # Se tiver encontrado cheiro de comida, segue pelo cheiro
        elif not possible_food:
            food_smells = max(
                food_smells,
                key=(lambda i: i[0])
            )
            self.model.grid.move_agent(self, food_smells[1])    
        # Se não, usa o caminho com a menor quantidade de feromônio e que
        # se encontra mais distante de casa.
        else:
            possible_food = min(
                possible_food,
                key=(lambda i: i[0] - (10 * calculate_distance(i[1], self.home)))
            )
            if possible_food[0] > self.model.min_pheromone_needed:
                self.model.grid.move_agent(self, possible_food[1])
            else:
                random_move(self)
