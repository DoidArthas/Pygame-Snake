import ResourceBundle as appleBundle
from pygame import Surface
from random import randint

values = appleBundle.get_bundle("apple")
size = int(values.get("apple_size"))
color = (int(values.get("RC")), int(values.get("GC")), int(values.get("BC")))
speed_increase = float(values.get("speed_increase"))


def collision_verify(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


def on_grid_random(width, height):
    x = randint(0, width * 10 - 1)
    y = randint(0, height * 10 - 1)
    return x * 10, y * 10


class apple:
    def __init__(self, screen_width_ratio, screen_height_ratio):
        self.surface = Surface((size, size))
        self.position = on_grid_random(screen_width_ratio, screen_height_ratio)
        self.surface.fill(color)

    def collision(self, gm, snake):
        if collision_verify(self.position, snake.position[0]):
            self.position = on_grid_random(gm.screenWidthRatio, gm.screenHeightRatio)
            snake.increase()
            gm.score = gm.score + 1
            gm.sleepTimeMS = gm.sleepTimeMS - speed_increase
