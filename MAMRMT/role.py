import random
import pygame
from pygame.locals import *
from MAMRMT.frame import *
import json
f = open('FieldInfo.ini', 'r')
text = f.read()
cfg = json.loads(text)
width = cfg['field']['field_width']
hight = cfg['field']['field_length']


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        index = random.randint(0, 3)
        if index == 0:
            image = pygame.image.load('source/JpPlane.png').convert()
        elif index == 1:
            image = pygame.image.load('source/GreenPlane.png').convert()
        elif index == 2:
            image = pygame.image.load('source/JitPlane.png').convert()
        else:
            image = pygame.image.load('source/LXPlane.png').convert()
        self.image = pygame.transform.scale(image, (32, 32))
        self.init_position = [16, 100, 200, 300, 400, 500, 600, 700, 784]  # 表示列
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(self.init_position[random.randint(0, 8)], 0))  # 从上往下，第0行，position为列
        # self.speed = random.randint(1, 2)
        self.speed = cfg['agent']['enemy']['enemy_speed']
        self.n_enemy = cfg['agent']['enemy']['n_enemy']

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > hight:
            self.kill()

    def get_pos(self):
        self.x = self.rect[0]
        self.y = self.rect[1]
        return self.x, self.y


class ManageAgent_pw(ManageAgent,pygame.sprite.Sprite):
    def __init__(self,roleId):
        ManageAgent.__init__(self,roleId)
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('source/GodPlane.png').convert()  # convert 转换像素格式
        self.image = pygame.transform.scale(image, (64, 64))  # transform 对图像翻转缩放旋转
        self.image.set_colorkey((255, 255, 255), RLEACCEL)  # 设置飞机透明度
        self.rect = self.image.get_rect(center=(width / 2, 500))  # set the plane's init position

    def update(self, action):
        if action == 0:                  # 原地不动
            self.rect.move_ip(0, 0)
        if action == 1:                  # 向上移动
            self.rect.move_ip(0, -5)
        if action == 2:                  # 向下移动
            self.rect.move_ip(0, 5)
        if action == 3:                  # 向左移动
            self.rect.move_ip(-5, 0)
        if action == 4:                  # 向右移动
            self.rect.move_ip(5, 0)
        # 限制plane的移动范围，不能超出屏幕
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > hight:
            self.rect.bottom = hight

    def get_pos(self):
        self.x = self.rect[0]
        self.y = self.rect[1]
        return self.x, self.y


class ExecuteAgent_pw(ExecuteAgent,pygame.sprite.Sprite):
    def __init__(self,roleId):
        ExecuteAgent.__init__(self,roleId)
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('source/mngPlane.png').convert()  # convert 转换像素格式
        self.image = pygame.transform.scale(image, (64, 64))  # transform 对图像翻转缩放旋转
        self.image.set_colorkey((255, 255, 255), RLEACCEL)  # 设置飞机透明度
        self.rect = self.image.get_rect(center=(width / 2, 500))  # set the plane's init position

    def get_pos(self):
        self.x = self.rect[0]
        self.y = self.rect[1]
        return self.x,self.y

    def update(self, action):
        if action == 0:                  # 原地不动
            self.rect.move_ip(0, 0)
        if action == 1:                  # 向上移动
            self.rect.move_ip(0, -5)
        if action == 2:                  # 向下移动
            self.rect.move_ip(0, 5)
        if action == 3:                  # 向左移动
            self.rect.move_ip(-5, 0)
        if action == 4:                  # 向右移动
            self.rect.move_ip(5, 0)
        # 限制plane的移动范围，不能超出屏幕
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > hight:
            self.rect.bottom = hight


def taskOrder(graph):
    in_degrees = dict((u, 0) for u in graph)  # 初始化所有顶点入度为0
    for u in graph:
        for v in graph[u]:
            in_degrees[v] += 1  # 计算每个顶点的入度
    Q = [u for u in in_degrees if in_degrees[u] == 0]  # 筛选入度为0的顶点
    Seq = []
    while Q:
        u = Q.pop()  # 默认从最后一个删除
        Seq.append(u)
        for v in graph[u]:
            in_degrees[v] -= 1  # 移除其所有指向
            if in_degrees[v] == 0:
                Q.append(v)  # 再次筛选入度为0的顶点
    return Seq


# 定义子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position):
        super(Bullet, self).__init__()
        image = pygame.image.load('source/bullet.png').convert()
        self.image = pygame.transform.scale(image, (16, 16))
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(center=(x_position, y_position))
        self.speed = cfg['agent']['bullet']['bullet_speed']

    def update(self):
        self.rect.move_ip(0, -self.speed)
        if self.rect.top < 0:
            self.kill()


# 定义云朵类
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.image = pygame.image.load('source/cloud.png').convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(center=(random.randint(0, width), 0))
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > hight + 50:
            self.kill()












