import pygame
import random


class Role:
    def __init__(self, roleId):
        self.roleId = roleId

    def composeTask(self, taskId, rank, status, target):
        self.task = Task(taskId, rank, status, target)

    def updateRole(self, targetRoleId):
        self.roleId = targetRoleId

    def assessCapacity(self, roleId):
        # if roleId == num,turn to capacity of corresponding role
        pass

    # def printId(self):
    #     print('the roleId is ',self.roleId,',corresponding taskId is ',self.roleId)

    def run(self):
        pass


class ManageAgent(Role):
    def __init__(self,roleId):
        super(ManageAgent, self).__init__(roleId)

    def receiveTask(self, task):
        # task 实际为需要击落的敌机数量
        # receiveTask 为 0 或者null，环境结束
        enemy_num = task
        return enemy_num

    def divideTask(self, taskList):
        # 敌机未出现时tasklist
        # 假设回传的taskList = [1,5,8,0,9,10]  1~50为飞机编号 , 0为观测任务
        last_task = []  # 记录历史未完成任务，若任务存在将任务优先级提高
        taskList = [1, 5, 8, 0, 9, 10]
        obs_task = 0
        att_task = []
        i = 0
        for t in taskList:
            if t == 0:
                obs_task += 1
            else:
                i += 1
                task = AttackTask(i, 1, 0, t)
                att_task.append(task)
        return att_task, obs_task

    def assignTask(self, observation, att_task, obs_task):
        # 算法输入为观测信息及任务需求（任务优先程度，任务难度，任务关系，任务限制），输出为每个agent的todo_taskList
        todo_list = DQN_task_assignment()  # todo_list = [[0],[1,5,10],[5,8,9]]
        return todo_list

    def releaseTask(self, todo_list):
        todo_list = [[0], [1, 5, 10], [5, 8, 9]]
        m_task = todo_list[0]
        e1_task = todo_list[1]
        e2_task = todo_list[2]

    def feedback(self, statu_list, todo_list):
        # 反馈的信息为任务状态，1为任务完成，返回已完成任务列表和未完成任务列表
        unfinished_task = []
        finished_task = []
        todo_list = [[0], [1, 5, 10], [5, 8, 9]]
        statu_list = [[1], [1, 0, 0], [0, 0, 0]]
        for i in statu_list:
            for j in i:
                if j == 0:
                    unfinished_task.append(todo_list[i][j])
                else:
                    finished_task.append(todo_list[i][j])
        return unfinished_task, finished_task

    def doTask(self, tasklist):
        pass


class ExecuteAgent(Role):
    def __init__(self, roleId):
        super(ExecuteAgent, self).__init__(roleId)

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
    def __init__(self, taskId, priority, status, target):
        self.taskId = taskId
        self.priority = priority
        self.status = status
        self.target = target

    def do(self, index):
        if index == 0:
            #  ObservationTask.do()
            pass
        elif index == 1:
            # AttackTask.do()
            pass
        elif index == 2:
            # TransmitTask.do()
            pass

    def updateStatus(self, newStatus):
        self.status = newStatus


class ObservationTask(Task):
    def __init__(self,taskId, priority, status, target, Oscope):
        Task.__init__(self,taskId, priority, status, target)
        self.Oscope = Oscope

    def do(self):
        print('observation')


class AttackTask(Task):
    def __init__(self, taskId, priority, status, target):
        Task.__init__(self, taskId, priority, status, target)

    def do(self):
        print('Attack')


class TransmitTask(Task):
    def __init__(self, taskId, priority, status, target, toRole):
        Task.__init__(self, taskId, priority, status, target)
        self.toRole = toRole

    def do(self):
        print('Transmit')


class Field:
    pass

