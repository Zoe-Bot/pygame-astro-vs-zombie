from init import * 

class Player:
    def __init__(self, x, y, speed, width, height, jump, direction, stepsRight, stepsLeft):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.jump = jump
        self.direction = direction #[links, rechts, stehen, sprung]
        self.stepsRight = stepsRight
        self.stepsLeft = stepsLeft
        self.isJumping = False
        self.lastDirection = [1, 0]
        self.okShooting = True

    def move(self, list):
        if list[0]:
            self.x -= self.speed
            self.direction = [1, 0, 0, 0]
            self.stepsLeft += 1
        if list[1]:
            self.x += self.speed
            self.direction = [0, 1, 0, 0]
            self.stepsRight += 1

    def resetSteps(self):
        self.stepsRight = 0
        self.stepsLeft = 0
        
    def stand(self):
        self.direction = [0, 0, 1, 0]
        self.resetSteps()

    def setJump(self):
        if self.jump == -16:
            self.isJumping = True
            self.jump = 15
            pygame.mixer.Sound.play(jumpSound)

    def jumping(self):
        if self.isJumping:
            self.direction = [0, 0, 0, 1]
            if self.jump >= -15:
                n = 1
                if self.jump < 0:
                    n = -1
                self.y-= (self.jump**2) * 0.17 * n
                self.jump -= 1
            else:
                self.isJumping = False

    def drawPlayer(self):
        if self.stepsRight == 63:
            self.stepsRight = 0
        if self.stepsLeft == 63:
            self.stepsLeft = 0

        if self.direction[0]:
            screen.blit(leftImg[self.stepsLeft//8], (self.x, self.y))
            self.lastDirection = [1, 0]

        if self.direction[1]:
            screen.blit(rightImg[self.stepsRight//8], (self.x, self.y))
            self.lastDirection = [0, 1]

        if self.direction[2]:
            if self.lastDirection[0]:
                screen.blit(attackLeftImg, (self.x, self.y))
            else:
                screen.blit(attackRightImg, (self.x, self.y))

        if self.direction[3]:
            screen.blit(jumpImg, (self.x, self.y))