from init import *

class Ball:
    def __init__(self, playerX, playerY, ballDirection, radius, color, ballSpeed):
        self.x = playerX
        self.y = playerY
        if ballDirection[0]:
            self.x += 5
            self.ballSpeed = ballSpeed * -1;
        elif ballDirection[1]:
            self.x += 92
            self.ballSpeed = ballSpeed
        self.y += 84
        self.radius = radius
        self.color = color

    def move(self):
        self.x += self.ballSpeed

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)
       