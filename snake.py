from pygame import Surface


class snake:
    def __init__(self):
        self.position = [(200, 200)]
        self.surface = Surface((10, 10))

        self.surface.fill((255, 255, 255))

        self.increase()
        self.increase()

    def increase(self):
        self.position.append((0, 0))

    def collision_verifier(self, screen):
        # Check if the snake collided with boundaries
        if self.position[0][0] == screen.get_width() or self.position[0][1] == screen.get_height() or \
                self.position[0][0] < 0 or self.position[0][1] < 0:
            return 1

        # Check if the snake has hit itself
        for i in range(1, len(self.position) - 1):
            if self.position[0][0] == self.position[i][0] and self.position[0][1] == self.position[i][1]:
                return 1

        return 0
