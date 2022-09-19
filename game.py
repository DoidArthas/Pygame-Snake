import ResourceBundle as gameBundle
from pygame import K_DOWN
from pygame import K_LEFT
from pygame import K_RIGHT
from pygame import K_UP
from pygame import display
from pygame import draw
from pygame import font
from pygame import init
from pygame import quit
from pygame import time
from pygame.locals import KEYDOWN
from pygame.locals import QUIT

values = gameBundle.get_bundle("values")


class game:
    def __init__(self):
        self.screenWidthRatio = int(values.get("screenWidth"))
        self.screenHeightRatio = int(values.get("screenHeight"))
        self.screenWidth = self.screenWidthRatio * 100
        self.screenHeight = self.screenHeightRatio * 100

        self.gameName = values.get("gameName")
        self.font_family = values.get("font-family")
        self.font_size = int(values.get("font-size"))

        self.sleepTimeMS = float(values.get("sleepTimeMs")) / 1000
        self.tick_rate = int(values.get("tickRate"))
        self.game_over = int(values.get("game_over"))
        self.score = int(values.get("score"))

        self.UP = int(values.get("UP"))
        self.RIGHT = int(values.get("RIGHT"))
        self.DOWN = int(values.get("DOWN"))
        self.LEFT = int(values.get("LEFT"))

        self.my_direction = self.LEFT

        self.screen = display.set_mode((self.screenWidth, self.screenHeight))
        display.set_caption(self.gameName)

        init()
        self.clock = time.Clock()

        self.font = font.Font(self.font_family, self.font_size)

    def print_at(self):
        print(f'|| {self.gameName} || {self.UP} || {self.RIGHT} || {self.DOWN} || {self.LEFT} ||')

    def event_handler(self, event):
        for new_event in event:
            # Caso o jogador feche o jogo.
            if new_event.type == QUIT:
                quit()
                exit()

            # Controla os eventos de tecla.
            if not self.game_over and new_event.type == KEYDOWN:
                self.key_handler(new_event)

    def key_handler(self, event):
        if event.key == K_UP and self.my_direction != self.DOWN:
            self.my_direction = self.UP
        if event.key == K_DOWN and self.my_direction != self.UP:
            self.my_direction = self.DOWN
        if event.key == K_LEFT and self.my_direction != self.RIGHT:
            self.my_direction = self.LEFT
        if event.key == K_RIGHT and self.my_direction != self.LEFT:
            self.my_direction = self.RIGHT

    def move(self, snake):
        if self.my_direction == self.UP:
            snake.position[0] = (snake.position[0][0], snake.position[0][1] - 10)
        if self.my_direction == self.DOWN:
            snake.position[0] = (snake.position[0][0], snake.position[0][1] + 10)
        if self.my_direction == self.RIGHT:
            snake.position[0] = (snake.position[0][0] + 10, snake.position[0][1])
        if self.my_direction == self.LEFT:
            snake.position[0] = (snake.position[0][0] - 10, snake.position[0][1])

    def draw_lines(self):
        for x in range(0, self.screenWidth, 10):  # Draw vertical lines
            draw.line(self.screen, (40, 40, 40), (x, 0), (x, self.screenHeight))
        for y in range(0, self.screenHeight, 10):  # Draw vertical lines
            draw.line(self.screen, (40, 40, 40), (0, y), (self.screenWidth, y))
