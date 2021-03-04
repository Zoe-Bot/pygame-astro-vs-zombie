import pygame
import sys #muss man nicht zwingend machen hilft oberflächen zu schließen

pygame.init() #initialisiert pygame

#initial stuff
screen = pygame.display.set_mode([1200, 595])
clock = pygame.time.Clock() #ist unabhängig von berechnung
pygame.display.set_caption("Pygame game")

#image load
bg = pygame.image.load("assets/background.png")
attackLeftImg = pygame.image.load("assets/player/angriffLinks.png")
attackRightImg = pygame.image.load("assets/player/angriffRechts.png")
jumpImg = pygame.image.load("assets/player/sprung.png")
rightImg = []
leftImg = []
for i in range(8):
    rightImg.append(pygame.image.load("assets/player/rechts" + str(i + 1) + ".png"))
    leftImg.append(pygame.image.load("assets/player/links" + str(i + 1) + ".png"))

#sound load
jumpSound = pygame.mixer.Sound("assets/sound/sprung.wav")

#wall für collision 
leftWall = pygame.draw.rect(screen, (0, 0, 0), (0, 0, 2, 600))
rightWall = pygame.draw.rect(screen, (0, 0, 0), (1198, 0, 2, 600))

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

#create player
player1 = Player(300, 393, 5, 96, 128, -16, [0, 0, 1, 0], 0, 0)

def draw():
    screen.blit(bg, (0, 0)) #setzt Hintergrund
    player1.drawPlayer()
    pygame.display.update() #macht änderung sichtbar

go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #macht das man spiel wieder schließen kann
            sys.exit()
    
    pressed = pygame.key.get_pressed() #alle aktuell gedrückte tasten
    playerRect = pygame.Rect(player1.x, player1.y, 96, 128)

    if pressed[pygame.K_RIGHT] and not playerRect.colliderect(rightWall):
        player1.move([0, 1])
    elif pressed[pygame.K_LEFT] and not playerRect.colliderect(leftWall):
        player1.move([1, 0])
    else:
        player1.stand()

    if pressed[pygame.K_UP]:
        player1.setJump()
    player1.jumping()

    draw()
    
    clock.tick(60) #framerate
    


