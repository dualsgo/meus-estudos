import pygame
import random
import sys

class Snake:
    def __init__(self, tile_count=10, initial_tail=4):
        self.tile_count = tile_count
        self.grid_size = 400 // tile_count
        self.initial_tail = initial_tail
        self.fixed_tail = True

        self.initial_player = (tile_count // 2, tile_count // 2)
        self.player = list(self.initial_player)
        self.velocity = [0, 0]

        self.walls = False
        self.fruit = [1, 1]

        self.trail = []
        self.tail = initial_tail

        self.points = 0
        self.points_max = 0

        self.action_enum = {'none': 0, 'up': 1, 'down': 2, 'left': 3, 'right': 4}
        self.last_action = self.action_enum['none']

    def reset(self):
        self.player = list(self.initial_player)
        self.velocity = [0, 0]
        self.tail = self.initial_tail
        self.points = 0
        self.trail.clear()
        self.trail.append(list(self.player))
        self.last_action = self.action_enum['none']
        self.random_fruit()

    def action(self, direction):
        if direction == 'up' and self.last_action != self.action_enum['down']:
            self.velocity = [0, -1]
        elif direction == 'down' and self.last_action != self.action_enum['up']:
            self.velocity = [0, 1]
        elif direction == 'left' and self.last_action != self.action_enum['right']:
            self.velocity = [-1, 0]
        elif direction == 'right' and self.last_action != self.action_enum['left']:
            self.velocity = [1, 0]

    def random_fruit(self):
        if self.walls:
            self.fruit = [1 + random.randint(0, self.tile_count - 3), 1 + random.randint(0, self.tile_count - 3)]
        else:
            self.fruit = [random.randint(0, self.tile_count - 1), random.randint(0, self.tile_count - 1)]

    def loop(self):
        reward = -0.1

        def dont_hit_wall():
            if self.player[0] < 0:
                self.player[0] = self.tile_count - 1
            if self.player[0] >= self.tile_count:
                self.player[0] = 0
            if self.player[1] < 0:
                self.player[1] = self.tile_count - 1
            if self.player[1] >= self.tile_count:
                self.player[1] = 0

        def hit_wall():
            if self.player[0] < 1 or self.player[0] > self.tile_count - 2 or \
                    self.player[1] < 1 or self.player[1] > self.tile_count - 2:
                self.reset()
                return True
            return False

        stopped = self.velocity == [0, 0]

        self.player[0] += self.velocity[0]
        self.player[1] += self.velocity[1]

        if self.velocity == [0, -1]:
            self.last_action = self.action_enum['up']
        elif self.velocity == [0, 1]:
            self.last_action = self.action_enum['down']
        elif self.velocity == [-1, 0]:
            self.last_action = self.action_enum['left']
        elif self.velocity == [1, 0]:
            self.last_action = self.action_enum['right']

        if self.walls:
            hit_wall()
        else:
            dont_hit_wall()

        if not stopped:
            self.trail.append(list(self.player))
            while len(self.trail) > self.tail:
                self.trail.pop(0)

        if not stopped:
            pass  # código relacionado à exibição na tela e interação do usuário

        for i in range(len(self.trail) - 1):
            if not stopped and self.trail[i] == self.player:
                self.reset()

        if self.player == self.fruit:
            if not self.fixed_tail:
                self.tail += 1
            self.points += 1
            if self.points > self.points_max:
                self.points_max = self.points
            reward = 1
            self.random_fruit()
            while self.fruit in self.trail:
                self.random_fruit()

        return reward

# Inicialização do pygame e configuração da janela
pygame.init()
tile_count = 10
screen_size = (400, 400)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

# Configurações do jogo
snake = Snake(tile_count)
snake.fixed_tail = False  # Define se a cauda da cobra cresce ao comer a fruta
snake.walls = False  # Define se o jogo terá paredes ou não

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.action('left')
            elif event.key == pygame.K_UP:
                snake.action('up')
            elif event.key == pygame.K_RIGHT:
                snake.action('right')
            elif event.key == pygame.K_DOWN:
                snake.action('down')
            elif event.key == pygame.K_SPACE:
                snake.velocity = [0, 0]
            elif event.key == pygame.K_ESCAPE:
                snake.reset()

    # Atualiza o estado do jogo e desenha na tela
    reward = snake.loop()

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(8)  # Taxa de quadros por segundo

pygame.quit()
sys.exit()
