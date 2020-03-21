import random
import pygame
from pygame.locals import *

width = 800
hight = 600

p_pos = []

class Role(pygame.sprite.Sprite):
    def __init__(self, roleId):
        super(Role,self).__init__()
        self.roleId = roleId

    def composeTask(self,taskId, rank, status):
        self.task = Task(taskId, rank, status)

    def updateRole(self, targetRoleId):
        self.roleId = targetRoleId

    def assessCapacity(self, roleId):
        # if roleId == num,turn to capacity of corresponding role
        pass

    def printId(self):
        print('the roleId is ',self.roleId,',corresponding taskId is ',self.roleId)

    def run(self):
        pass

# 定义Player类,sprite为操作移动图像类，即agent类
class Player(Role):
    def __init__(self, roleId):
        Role.__init__(self, roleId)    # 继承sprite的初始化

    def update(self, action):
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
        elif self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > hight:
            self.rect.bottom = hight


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
        self.init_position = [10, 100, 200, 300, 400, 500, 600, 700, 790]  # 表示列
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(self.init_position[random.randint(0, 8)], 0)) # 从上往下，第0行，position为列
        # self.speed = random.randint(1, 2)
        self.speed = 1
        self.n_enemy = 100

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > hight:
            self.kill()

class obs_rec(pygame.sprite.Sprite):
    def __init__(self):
        self.color = (0, 0, 0, 0)
        self.rect = ()


class ManageAgent(Player):
    def __init__(self, roleId):
        Player.__init__(self, roleId)
        image = pygame.image.load('source/GodPlane.png').convert()  # convert 转换像素格式
        self.image = pygame.transform.scale(image, (64, 64))  # transform 对图像翻转缩放旋转
        self.image.set_colorkey((255, 255, 255), RLEACCEL)  # 设置飞机透明度
        self.rect = self.image.get_rect(center=(width / 3, 500))  # set the plane's init position
        self.obs_size = 100


    def receiveTask(self, taskList):
        pass

    def divideTask(self):
        pass

    def releaseTask(self):
        # according taskId assign to role
        pass

    def assignTask(self):
        pass

    def feedback(self):
        pass


class ExecuteAgent(Player):
    def __init__(self, roleId):
        Player.__init__(self, roleId)
        image = pygame.image.load('source/mngPlane.png').convert()  # convert 转换像素格式
        self.image = pygame.transform.scale(image, (64, 64))  # transform 对图像翻转缩放旋转
        self.image.set_colorkey((255, 255, 255), RLEACCEL)  # 设置飞机透明度
        self.rect = self.image.get_rect(center=(width *2 / 3, 500))  # set the plane's init position
        # self.Rect.copy = self.rect.copy
        self.obs_size = 20

    def executeTask(self,nature):
        # if nature == num,turn to execute corresponding action
        return '完成'

    def noticeMngAgent(self):
        pass

    def receiveMsg(self):
        pass

    def exceptionHandle(self):
        pass


class Task:
    def __init__(self, taskId, rank, status):
        self.taskId = taskId
        self.rank = rank
        self.status = status

    def init(self):
        pass

    def updateStatus(self, newStatus):
        self.status = newStatus


# class ObservationTask(Task):
#     def __init__(self, taskId, rank, status, deadline, etiTime, target, vision):
#         Task.__init__(self, taskId, rank, status, deadline, etiTime, target)
#         self.vision = vision
#
#
# class ContactTask(Task):
#     def __init__(self, taskId, rank, status, deadline, etiTime, target, endStatus, targetEndWt):
#         Task.__init__(self, taskId, rank, status, deadline, etiTime, target)
#         self.endStatus = endStatus
#         self.targetEndWt = targetEndWt
#
#
# class DeliverTask(Task):
#     def __init__(self, taskId, rank, status, deadline, etiTime, target, targetEndwt, relSpeed):
#         Task.__init__(self, taskId, rank, status, deadline, etiTime, target)
#         self.targetEndwt = targetEndwt
#         self.relSpeed = relSpeed
#
#
# class TransmitTask(Task):
#     def __init__(self, taskId, rank, status, deadline, etiTime, target, toRole, news):
#         Task.__init__(self, taskId, rank, status, deadline, etiTime, target)
#         self.toRole = toRole
#         self.news = news


# 定义子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position):
        super(Bullet, self).__init__()
        image = pygame.image.load('source/bullet.png').convert()
        self.image = pygame.transform.scale(image, (16, 16))
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(center=(x_position, y_position))
        self.speed = 2

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


# if __name__ == '__main__':
#     r1 = Role(0, 1)  # capacity 1 is attack
#     r1.printId()
#     r1.composeTask(0, 0,'未完成')
#     r2 = Role(1, -1)
#     r2.printId()
#     r2.composeTask(1, 0,'未完成')
#     x = random.randint(0, 1)
#     assignMAE(x)
#










