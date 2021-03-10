from init import * 
from player import Player
from ball import Ball
from zombie import Zombie

#create player
player1 = Player(300, 393, 5, 96, 128, -16, [0, 0, 1, 0], 0, 0)

#create zombie
zombie1 = Zombie(600, 393, 4, 96, 128, [0, 0], 40, 1090)

#create ball
balls = []

def draw():
    screen.blit(bg, (0, 0)) #setzt Hintergrund
    for k in balls:
        k.draw()
    player1.drawPlayer()
    zombie1.lifeZombie()
    zombie1.drawZombie()
    pygame.display.update() #macht änderung sichtbar

go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #macht das man spiel wieder schließen kann
            sys.exit()
    
    #vars
    pressed = pygame.key.get_pressed() #alle aktuell gedrückte tasten
    playerRect = pygame.Rect(player1.x, player1.y, 96, 128)
    zombieRect = pygame.Rect(zombie1.x + 18, zombie1.y + 24, zombie1.width - 36, zombie1.height - 24)

    #player movement
    if pressed[pygame.K_RIGHT] and not playerRect.colliderect(rightWall):
        player1.move([0, 1])
    elif pressed[pygame.K_LEFT] and not playerRect.colliderect(leftWall):
        player1.move([1, 0])
    else:
        player1.stand()

    #player jump
    if pressed[pygame.K_UP]:
        player1.setJump() 
    player1.jumping()

  
       #shooting
    if pressed[pygame.K_SPACE]:
        if len(balls)  <= 4 and player1.okShooting:
            balls.append(Ball(round(player1.x), round(player1.y), player1.lastDirection, 8, (10, 10, 10), 7))
        player1.okShooting = False

    if not pressed[pygame.K_SPACE]:
        player1.okShooting = True

    
    for k in balls:
        #let shoot ball moves and remove them out of screen
        if k.x >= 0 and k.x <= 1200:
            k.move()
        else:
            balls.remove(k)

        ballRect = pygame.Rect(k.x - k.radius, k.y - k.radius, k.radius * 2, k.radius * 2)
        if zombieRect.colliderect(ballRect):
            balls.remove(k)
            zombie1.life -= 1
        

    zombie1.turnAround()
    draw()
    
    clock.tick(60) #framerate
    


