import pygame
import sys
import random

from Sprites2D import *
from ObjectBehavior import *
from CONSTANTS import *
from UI import *

        
def main():
    GameOver = False
    pygame.init()  
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    mainClock = pygame.time.Clock()
    player = Player((0, 0), [64, 64], BLUE)
    pistole = Pistole()
    ammoStatus = Text()
    
    mainGroup = pygame.sprite.Group()
    enemyGroup = pygame.sprite.Group()
    bulletGroup = pygame.sprite.Group()
    mainGroup.add(player)
    
        
    while(not GameOver):

        mainClock.tick(60)
        if not enemyGroup.sprites():
            for i in range(1, 10):
                enemy = Enemy((random.randrange(SCREEN_WIDTH, SCREEN_WIDTH+400), random.randrange(0, SCREEN_HEIGHT-10)),
                              [64, 64], RED)
                mainGroup.add(enemy)
                enemyGroup.add(enemy)
                
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    player.y_direction = 1
                elif event.key == pygame.K_w:
                    player.y_direction = -1
                if event.key == pygame.K_a:
                    player.x_direction = -1
                elif event.key == pygame.K_d:
                    player.x_direction = 1
                if event.key == pygame.K_r:
                    pistole.reload()
                if event.key == pygame.K_ESCAPE:
                    GameOver == True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    player.y_direction = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    player.x_direction = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                pistole.fire(player.rect.center, mainGroup, bulletGroup)

            if event.type == pygame.QUIT:
                GameOver = True
                
        screen.fill((0, 100, 0))
        screen.blit(ammoStatus.display('Ammo: '+str(pistole.bullets)+'/7'), (10, 0))
        pygame.sprite.groupcollide(bulletGroup, enemyGroup, dokilla=True, dokillb=True)
        mainGroup.update()
        mainGroup.draw(screen)
        pygame.display.update()

    pygame.quit()
    sys.exit()
    
if __name__ == '__main__':
    main()
