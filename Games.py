import pygame
import sys

class Game(object):

    def __init__(self, window_size, fps):
        pygame.init()
        self.game_over = False
        self.window_size = window_size
        self.fps = fps
        self.screen = pygame.display.set_mode(self.window_size)
        self.clock = pygame.time.Clock()
        self.seconds_per_frame = 0

    def update(self):
        pygame.display.update()
        self.seconds_per_frame = self.clock.tick(self.fps)/1000

    def quit(self):
        pygame.quit()
        sys.exit()
