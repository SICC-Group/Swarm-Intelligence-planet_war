import random
import pygame
from pygame.locals import *
from Swarm_Intelligence_planet_war.MAMRMT.frame.Task import *

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
        self.rect = self.image.get_rect(center=(400, 500))  # set the plane's init position
        self.obs_size = 100

    def receiveTask(self, task):
        # task 实际为需要击落的敌机数量
        # receiveTask 为 0 或者null，环境结束
        enemy_num = task
        print("任务数量：",enemy_num)

    def divideTask(self,taskList):
        # 敌机未出现时tasklist
        # 假设回传的taskList = [1,5,8,0,9,10]  1~50为飞机编号 , 0为观测任务
        last_task = []  # 记录历史未完成任务，若任务存在将任务优先级提高
        obs_task = 0
        att_task = []
        i = 0
        for t in taskList:
            if t == 0:
                obs_task += 1
            else:
                i += 1
                task = AttackTask(i, 1, 0, t)
                # task = (i, 1, 0, t)
                att_task.append(task)
        return att_task, obs_task

    def assignTask(self, agt_pos, att_task, obs_task, emy_pos_dic):
        mngtask = [0]
        exe1task = []
        exe2task = []
        todo_list = []
        todo_list.append(mngtask)
        emy_id = 0
        if len(att_task)>0:
        # 算法输入为观测信息及任务需求（任务优先程度，任务难度，任务关系，任务限制），输出为agent的todo_taskList todo_list = [[0],[1,5,10],[5,8,9]]
            for att_t in att_task:
                emy_id = att_t.target
                emy_pos = emy_pos_dic[emy_id]
                dist_list = []
                for exe_a in agt_pos[:2]:
                    value = abs(emy_pos[0] - exe_a[0])
                    dist_list.append(value)
                role_num = dist_list.index(min(dist_list))
                if role_num == 0:
                    exe1task.append(att_t)
                elif role_num == 1:
                    exe2task.append(att_t)
            todo_list.append(exe1task)
            todo_list.append(exe2task)
        return todo_list

    def releaseTask(self,todo_list):
        mngtask = todo_list[0]
        exe1task = todo_list[1]
        exe2task = todo_list[2]

    # def feedback(self,statu_list,todo_list):
    #     # 反馈的信息为任务状态，1为任务完成，返回已完成任务列表和未完成任务列表
    #     unfinished_task = []
    #     finished_task = []
    #     todo_list = [[0], [1, 5, 10], [5, 8, 9]]
    #     statu_list = [[1], [1, 0, 0], [0, 0, 0]]
    #     for i in statu_list:
    #         for j in i:
    #             if j == 0:
    #                 unfinished_task.append(todo_list[i][j])
    #             else:
    #                 finished_task.append(todo_list[i][j])
    #     return unfinished_task,finished_task
    #
    # def doTask(self,tasklist):
    #     pass

class ExecuteAgent(Role):
    def __init__(self, roleId):
        Role.__init__(self, roleId)
        image = pygame.image.load('../source/mngPlane.png').convert()  # convert 转换像素格式
        self.image = pygame.transform.scale(image, (64, 64))  # transform 对图像翻转缩放旋转
        self.image.set_colorkey((255, 255, 255), RLEACCEL)  # 设置飞机透明度
        self.rect = self.image.get_rect(center=(100, 400))  # set the plane's init position
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
    pass
    # def assignTask(self,task):
    #     pass

class ExecuteGenetic(ExecuteAgent):
    def execute(self, agent_pose, tasklist, emy_pos_dic):
        for i in tasklist:
            dist = emy_pos_dic[i][0] - agent_pose[0]
            if (dist > 0):
                action = 4  # right
            elif (dist < 0):
                action = 3  # left
            else:
                action = 0  # still
        return action

'''DQN'''
class ManagerDQN(ManagerAgent):
    pass

class ExecuteDQN(ExecuteAgent):
    def execute(self):
        print("Agent"+str(self.roleId)+"ExecuteDQN")












