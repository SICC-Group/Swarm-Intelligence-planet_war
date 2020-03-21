import random
import pygame
from pygame.locals import *

class Role(pygame.sprite.Sprite):
    def __init__(self, roleId):
        super(Role,self).__init__()
        self.roleId = roleId

    def update(self, action,size):
        if action == 0:
            self.rect.move_ip(0, 0)
        if action == 1:
            self.rect.move_ip(0, -10)
        if action == 2:
            self.rect.move_ip(0, 10)
        if action == 3:
            self.rect.move_ip(-10, 0)
        if action == 4:
            self.rect.move_ip(10, 0)
        # 限制plane的移动范围，不能超出屏幕
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > size[0]:
            self.rect.right = size[0]
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > size[1]:
            self.rect.bottom = size[1]

    def run(self):
        pass

class ManagerAgent(Role):
    def __init__(self, roleId):
        Role.__init__(self, roleId)
        image = pygame.image.load('../source/GodPlane.png').convert()  # convert 转换像素格式
        self.image = pygame.transform.scale(image, (64, 64))  # transform 对图像翻转缩放旋转
        self.image.set_colorkey((255, 255, 255), RLEACCEL)  # 设置飞机透明度
        self.rect = self.image.get_rect(center=(800/3, 500))  # set the plane's init position
        self.obs_size = 100


class ExecuteAgent(Role):
    def __init__(self, roleId):
        Role.__init__(self, roleId)
        image = pygame.image.load('../source/mngPlane.png').convert()  # convert 转换像素格式
        self.image = pygame.transform.scale(image, (64, 64))  # transform 对图像翻转缩放旋转
        self.image.set_colorkey((255, 255, 255), RLEACCEL)  # 设置飞机透明度
        self.rect = self.image.get_rect(center=(800*2 / 3, 500))  # set the plane's init position
        self.obs_size = 20

    def execute(self):
        pass

class ManagerContractNet(ManagerAgent):
    print("ContractNet")

class ExecuteContractNet(ExecuteAgent):
    def execute(self):
        print("Agent"+str(self.roleId)+"ExecuteContractNet")

'''遗传算法'''
class ManagerGenetic(ManagerAgent):
    def assignTask(self,task):
        pass

class ExecuteGenetic(ExecuteAgent):
    def execute(self):
        pass

'''DQN'''
class ManagerDQN(ManagerAgent):
    def assignTask(self,task):
        pass

class ExecuteDQN(ExecuteAgent):
    def execute(self):
        pass












