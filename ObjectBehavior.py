from Sprites2D import Bullet
from CONSTANTS import *

class Pistole(object):
    def __init__(self):
        self.bullets = 7

    def fire(self, bulletSpawnPoint, *Groups):
        if self.bullets == 0:
            print('Reload')
        else:
            self.bullets -= 1
            bullet = Bullet(bulletSpawnPoint, [5, 5], WHITE)
            for group in Groups:
                group.add(bullet)

    def reload(self):
        self.bullets = 7
