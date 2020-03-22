import random
import pygame


class Task:
    '''
        task编号
        优先级
        状态
        最晚开始时间
        预估执行时间
        目标
    '''
    def __init__(self, taskId, priority, status, target):
        self.taskId = taskId
        self.priority = priority
        self.status = status
        # self.startTime=startTime
        # self.executeTime=executeTime
        self.target = target

    def updateStatus(self, status):
        self.status = status
        if status == 0:
            status = 1



class ShootTask(Task):
    def __init__(self, taskId, priority, status, target):
        Task.__init__(self, taskId, priority, status, target)
        # taskId:1--50
        self.priority = 1

    def track(self, agent, enemy):
        dist = enemy.rect[0] - agent.rect[0]
        if (dist > 0):
            action = 4   # right
        elif(dist < 0):
            action = 3  # left
        else:
            action = 0   #still
        return action


class ObserveTask(Task):
    def __init__(self, taskId, priority, status, target):
        Task.__init__(self, 0, 2, status, target)
        self.taskId = 0
        self.priority = 2

    def get_obs(self):
        self.x = self.rect[0]
        self.y = self.rect[1]
        return self.x,self.y


