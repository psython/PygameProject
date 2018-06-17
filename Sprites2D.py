import pygame
import sys
import random

from CONSTANTS import *


class Object_2D(pygame.sprite.Sprite):

    def __init__(self, spawnPoint, size, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = spawnPoint[0]
        self.rect.y = spawnPoint[1]
        self.spawnPoint = spawnPoint

    def load_image(self, imagePath):
        self.image = pygame.image.load(imagePath).convert_alpha()
        #return self.image
class Item(Object_2D):

    def __init__(self, spawnPoint, size, color):
        Object_2D.__init__(self, spawnPoint, size, color)

class Bullet(Object_2D):

    def __init__(self, spawnPoint, direction, size, color):
        Object_2D.__init__(self, spawnPoint, size, color)
        self.speed = 45
        self.direction = direction
        self.steigung = (self.direction[1]-self.spawnPoint[1])/(self.direction[0]-self.spawnPoint[0])
        print(self.steigung)
        self.yS = self.steigung*self.spawnPoint[0]-self.spawnPoint[1]

    def update(self):
        self.rect.x += self.speed
        self.rect.y = self.rect.x*self.steigung-self.yS
        if self.rect.x > SCREEN_WIDTH:
            self.kill()

class Enemy(Object_2D):

    def __init__(self, spawnPoint, size, color):
        Object_2D.__init__(self, spawnPoint, size, color)
        self.speed = random.randrange(1, 4)
        self.health = 3

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < -128:
            self.kill()
        if self.health == 0:
            die_sound = pygame.mixer.Sound('die.wav')
            die_sound.play()
            self.kill()

    def collide(self, collision_group):
        for sprite in collision_group:
            if self.rect.colliderect(sprite.rect):
                sprite.kill()
                prehit_sound = pygame.mixer.Sound('prehit.wav')
                prehit_sound.play()
                self.health -= 1

class Player(Object_2D):

    def __init__(self, spawnPoint, size, color):
        Object_2D.__init__(self, spawnPoint, size, color)
        self.speed = 5
        self.health = 5
        self.x_direction = 0
        self.y_direction = 0
        self.inventory = {'Bullets' : 120}

    def collide(self, collision_group):
        for sprite in collision_group:
            if self.rect.colliderect(sprite.rect):
                die_sound = pygame.mixer.Sound('dead.wav')
                die_sound.play()

    def update(self):
        self.rect.x += self.speed * self.x_direction
        self.rect.y += self.speed * self.y_direction
        if self.rect.x <= 0:
            self.rect.x = 1
            self.x_direction = 0
        if self.rect.y <= 0:
            self.rect.y = 1
            self.y_dircetion = 0
        if self.rect.y >= SCREEN_HEIGHT-128:
            self.rect.y = SCREEN_HEIGHT-129
            self.y_direction = 0
