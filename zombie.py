from init import *

class Zombie:
    def __init__(self, x, y, zombieSpeed, width, height, direction, xMin, xMax):
        self.x = x
        self.y = y
        self.zombieSpeed = zombieSpeed
        self.width = width
        self.height = height
        self.direction = direction
        self.stepsRight = 0
        self.stepsLeft = 0
        self.xMin = xMin
        self.xMax = xMax
        self.life = 6
        self.fullLife = pygame.image.load("assets/heart/voll.png")
        self.halfLife = pygame.image.load("assets/heart/halb.png")
        self.emptyLife = pygame.image.load("assets/heart/leer.png")
        self.leftImg = []
        self.rightImg = []

        for i in range(8):
            self.rightImg.append(pygame.image.load("assets/enemie/r" + str(i + 1) + ".png"))
            self.leftImg.append(pygame.image.load("assets/enemie/l" + str(i + 1) + ".png"))

    def lifeZombie(self):
        if self.life >= 2:
            screen.blit(self.fullLife, (507, 15))
        if self.life >= 4:    
            screen.blit(self.fullLife, (569, 15))
        if self.life == 6:
            screen.blit(self.fullLife, (631, 15))

        if self.life == 1:
            screen.blit(self.halfLife, (507, 15))
        elif self.life == 3:
            screen.blit(self.halfLife, (569, 15))
        elif self.life == 5:
            screen.blit(self.halfLife, (631, 15))

        if self.life <= 0: 
            screen.blit(self.emptyLife, (507, 15))
        if self.life <= 2: 
            screen.blit(self.emptyLife, (569, 15))
        if self.life <= 4: 
            screen.blit(self.emptyLife, (631, 15))

    def drawZombie(self):
        if self.stepsRight == 63:
            self.stepsRight = 0

        if self.stepsLeft == 63:
            self.stepsLeft = 0

        if self.direction[0]:
            screen.blit(self.leftImg[self.stepsLeft // 8], (self.x, self.y))
        if self.direction[1]:
            screen.blit(self.rightImg[self.stepsRight // 8], (self.x, self.y))

    def move(self):
        self.x += self.zombieSpeed

        if self.zombieSpeed > 0:
            self.direction = [0, 1]
            self.stepsRight += 1
        if self.zombieSpeed < 0:
            self.direction = [1, 0]
            self.stepsLeft += 1

    def turnAround(self):
        if self.x > self.xMax:
            self.zombieSpeed *= -1
        elif self.x < self.xMin:
            self.zombieSpeed *= -1
        self.move()

    def collisionBox(self):
        
