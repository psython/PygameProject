import pygame
from CONSTANTS import *

class Scene(object):

    def __init__(self, mainSurface):
        self.mainSurface = mainSurface
        self._background = None
        self.images = []

    def update_Scene(self, *spriteGroups):

        self.mainSurface.fill(BLACK)

        if self._background != None:
            self.mainSurface.blit(self._background, (0, 0))

        for spriteGroup in spriteGroups:
            spriteGroup.update()
            spriteGroup.draw(self.mainSurface)

        for image, position in self.images:
            self.mainSurface.blit(image, position) #position variabel

        self.images = []

    def enable_Background(self, backgroundImage):
        self._background = pygame.image.load(backgroundImage).convert()


    def add_sprite(self, sprite, position):
        self.images.append((sprite, position))
