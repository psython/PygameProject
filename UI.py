import pygame

from CONSTANTS import *

class Text(object):

    def __init__(self):
        self.font = pygame.font.SysFont('comicsansms', 50)

    def display(self, text):
        return self.font.render(text, True, WHITE)
