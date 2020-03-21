import pygame
from pygame.locals import *
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self,size):
        super(Enemy, self).__init__()
        self.size=size
        index = random.randint(0, 3)
        if index == 0:
            image = pygame.image.load('../source/JpPlane.png').convert()
        elif index == 1:
            image = pygame.image.load('../source/GreenPlane.png').convert()
        elif index == 2:
            image = pygame.image.load('../source/JitPlane.png').convert()
        else:
            image = pygame.image.load('../source/LXPlane.png').convert()
        self.image = pygame.transform.scale(image, (32, 32))
        self.init_position = [10, 100, 200, 300, 400, 500, 600, 700, 790]  # 表示列
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(self.init_position[random.randint(0, 8)], 0)) # 从上往下，第0行，position为列
        self.speed = 1
        self.n_enemy = 100

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >self.size[1]:
            self.kill()

# 定义云朵类
class Cloud(pygame.sprite.Sprite):
    def __init__(self,size):
        super(Cloud, self).__init__()
        self.size=size
        self.image = pygame.image.load('../source/cloud.png').convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(center=(random.randint(0,self.size[0]), 0))
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > self.size[1] + 50:
            self.kill()

# 定义子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position):
        super(Bullet, self).__init__()
        image = pygame.image.load('../source/bullet.png').convert()
        self.image = pygame.transform.scale(image, (16, 16))
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(center=(x_position, y_position))
        self.speed = 2

    def update(self):
        self.rect.move_ip(0, -self.speed)
        if self.rect.top < 0:
            self.kill()
