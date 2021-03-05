import pygame
import sys

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