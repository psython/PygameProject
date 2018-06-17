from Sprites2D import *
from CONSTANTS import *


class Pistole(object):
    def __init__(self):
        self.bullets = 12
        self.magazine_size = 12
        self.reloading = False
        self.reloading_time = 0.1

    def fire(self, bulletSpawnPoint, *Groups):
        if self.bullets == 0:
            print('Reload')
        elif not self.reloading:
            aim_point = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]
            self.bullets -= 1
            bullet = Bullet(bulletSpawnPoint, aim_point, [10, 10], GREEN)
            for group in Groups:
                group.add(bullet)

    def reload(self, inventory, delta):
        if inventory['Bullets'] > 0 and self.reloading == True and self.bullets < self.magazine_size:
            if self.reloading_time > 0:
                self.reloading_time -= delta
            elif self.reloading_time <= 0:
                reloading_sound = pygame.mixer.Sound('reload.wav')
                reloading_sound.play()
                self.bullets += 1
                inventory['Bullets'] -= 1
                self.reloading_time = 0.1

            if inventory['Bullets'] == 0 or self.bullets == self.magazine_size:
                self.reloading = False
                self.reloading_time = 0.1
        else:
            self.reloading = False
            self.reloading_time = 0.1
