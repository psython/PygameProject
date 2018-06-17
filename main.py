import pygame
import sys, os
import random

from Sprites2D import *
from ObjectBehavior import *
from CONSTANTS import *
from UI import *
from Scenes import *
from Games import *


def main():

    newGame = Game([SCREEN_WIDTH, SCREEN_HEIGHT], 60)

    mainScene = Scene(newGame.screen)
    mainScene.enable_Background('background.png')

    spriteSize = [128, 128]
    player = Player((SCREEN_WIDTH/2, SCREEN_HEIGHT/2), spriteSize, BLUE)
    player.load_image('player.png')
    pistole = Pistole()
    ammoStatus = Text()
    reloadingText = Text()
    counter_Text = Text()

    playerGroup = pygame.sprite.Group()
    enemyGroup = pygame.sprite.Group()
    bulletGroup = pygame.sprite.Group()
    playerGroup.add(player)

    shoot_sound = pygame.mixer.Sound('shoot.wav')
    zombies = 1
    counter = 0

    while not newGame.game_over:

        if not enemyGroup.sprites():
            for i in range(0, zombies):
                enemy = Enemy((random.randrange(SCREEN_WIDTH, SCREEN_WIDTH+400), random.randrange(0, SCREEN_HEIGHT-128)),
                              spriteSize, RED)
                enemy.load_image('zombie.png')
                enemyGroup.add(enemy)
            zombies += 1

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    player.y_direction = 1
                if event.key == pygame.K_w:
                    player.y_direction = -1
                if event.key == pygame.K_a:
                    player.x_direction = -1
                if event.key == pygame.K_d:
                    player.x_direction = 1
                if event.key == pygame.K_r:
                    pistole.reloading = True
                if event.key == pygame.K_ESCAPE:
                    newGame.game_over = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    player.y_direction = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    player.x_direction = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                shoot_sound.play()
                pistole.fire(player.rect.topright, bulletGroup)

            if event.type == pygame.QUIT:
                newGame.game_over = True

        pistole.reload(player.inventory, newGame.seconds_per_frame)
        mainScene.update_Scene(enemyGroup, bulletGroup, playerGroup)
        if pistole.reloading == True:
            mainScene.add_sprite(reloadingText.display('Reloading...'), player.rect.topleft)
        mainScene.add_sprite(ammoStatus.display('Ammo: '+str(pistole.bullets)+'/12'), [0, 0])
        mainScene.add_sprite(counter_Text.display(str(int(counter))), [SCREEN_WIDTH/2, 0])
        for enemy in enemyGroup:
            enemy.collide(bulletGroup)
            player.collide(enemyGroup)

        newGame.update()
        counter += newGame.seconds_per_frame
    newGame.quit()

if __name__ == '__main__':
    main()
