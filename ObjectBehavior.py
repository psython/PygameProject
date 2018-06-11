from Sprites2D import Bullet
from CONSTANTS import *

class Pistole(object):
    def __init__(self):
        self.bullets = 12

    def fire(self, bulletSpawnPoint, *Groups):
        if self.bullets == 0:
            print('Reload')
        else:
            self.bullets -= 1
            bullet = Bullet(bulletSpawnPoint, [10, 10], RED)
            for group in Groups:
                group.add(bullet)

    def reload(self):
        self.bullets = 12
