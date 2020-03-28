import pygame
from pygame.locals import *

class Role(pygame.sprite.Sprite):
    def __init__(self, roleId):
        super(Role,self).__init__()
        self.roleId = roleId


class ManagerAgent(Role):
    def __init__(self, roleId):
        Role.__init__(self, roleId)
        image = pygame.image.load('../source/GodPlane.png').convert()  # convert 转换像素格式
        self.image = pygame.transform.scale(image, (64, 64))  # transform 对图像翻转缩放旋转
        self.image.set_colorkey((255, 255, 255), RLEACCEL)  # 设置飞机透明度
        self.rect = self.image.get_rect(center=(400, 400))  # set the plane's init position
        self.obs_size = 400

    def doTask(self,task,enemy):
        m_obs = pygame.Rect(0, 0, 0, 0)
        m_obs = self.rect.copy()
        # 原位置放大后的矩形
        m_obs.inflate_ip(self.obs_size,self.obs_size)
        return task.doTask(m_obs,enemy)

    def assignTask(self, data):
        task = {}
        # 判断exeAgent观测的敌机
        for key in data[0].keys():
            if (key != 'm'):
                if (len(data[1]) == 0):
                    task[key] = 0
                elif (data[0][key][1] <= data[1][0][1]):
                    del (data[1][0])
                    task[key] = 0
                else:
                    task[key] = data[1][0][0] - data[0][key][0]
                    del (data[1][0])
        return task

class ExecuteAgent(Role):
    def __init__(self, roleId):
        Role.__init__(self, roleId)
        image = pygame.image.load('../source/mngPlane.png').convert()  # convert 转换像素格式
        self.image = pygame.transform.scale(image, (64, 64))  # transform 对图像翻转缩放旋转
        self.image.set_colorkey((255, 255, 255), RLEACCEL)  # 设置飞机透明度
        self.rect = self.image.get_rect(center=(200+self.roleId*100,550))  # set the plane's init position
        self.obs_size = 100

    def doTask(self,task,enemy):
        e_ob = pygame.Rect(0, 0, 0, 0)
        e_ob = self.rect.copy()
        e_ob.inflate_ip(self.obs_size,self.obs_size)
        return task.doTask(e_ob,enemy)

    def execute(self, distance, action):
        pass


class ManagerContractNet(ManagerAgent):
    print("ContractNet")


class ExecuteContractNet(ExecuteAgent):
    def execute(self, distance, action):
        if action == 0:
            self.rect.move_ip(0, 0)
        elif action == 1:
            self.rect.move_ip(0, distance)
        elif action == 2:
            self.rect.move_ip(distance, 0)

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












