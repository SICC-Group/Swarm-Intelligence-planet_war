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
    def __init__(self,taskId, priority,status,target):
        self.taskId=taskId
        self.priority=priority
        self.status=status
        # self.startTime=startTime
        # self.executeTime=executeTime
        self.target=target

    def updateStatus(self,status):
        self.status=status
        if status == 0 :
            print("任务未完成")
        else:
            print("任务已完成")

    def taskOrder(self,graph):
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


class ObservationTask(Task):
    def __init__(self, taskId, rank, status, deadline, etiTime, target, vision):
        Task.__init__(self, taskId, rank, status, deadline, etiTime, target)
        self.taskId = 2
        self.rank = 2
        self.obs_size = 100
        self.vision = vision
    def get_obs(self):
        self.x = self.rect[0]
        self.y = self.rect[1]
        return self.x,self.y

class ShootTask(Task):
    def __init__(self, taskId, rank, status, deadline, etiTime, target, vision):
        Task.__init__(self, taskId, rank, status, deadline, etiTime, target)
        self.taskId = 1
        self.rank = 1
        self.vision = vision
    def track(self,enemy):
        action =  action = random.randint(0, 4)
        return action

# class ContactTask(Task):
#     def __init__(self, taskId, rank, status, deadline, etiTime, target, endStatus, targetEndWt):
#         Task.__init__(self, taskId, rank, status, deadline, etiTime, target)
#         self.endStatus = endStatus
#         self.targetEndWt = targetEndWt


# class DeliverTask(Task):
#     def __init__(self, taskId, rank, status, deadline, etiTime, target, targetEndwt, relSpeed):
#         Task.__init__(self, taskId, rank, status, deadline, etiTime, target)
#         self.targetEndwt = targetEndwt
#         self.relSpeed = relSpeed


# class TransmitTask(Task):
#     def __init__(self, taskId, rank, status, deadline, etiTime, target, toRole, news):
#         Task.__init__(self, taskId, rank, status, deadline, etiTime, target)
#         self.toRole = toRole
#         self.news = news













graph={'1':'234','2':'5','3':'25','4':'35','5':''}
task_list=taskOrder(graph)
if(len(task_list)==len(graph)):
    manager.acceptTask(task_list)
else:
    print("there is a circle.")


# def taskOrder(self,graph):
#     in_degrees = dict((u, 0) for u in graph)  # 初始化所有顶点入度为0
#     for u in graph:
#         for v in graph[u]:
#             in_degrees[v] += 1  # 计算每个顶点的入度
#     Q = [u for u in in_degrees if in_degrees[u] == 0]  # 筛选入度为0的顶点
#     Seq = []
#     while Q:
#         u = Q.pop()  # 默认从最后一个删除
#         Seq.append(u)
#         for v in graph[u]:
#             in_degrees[v] -= 1  # 移除其所有指向
#             if in_degrees[v] == 0:
#                 Q.append(v)  # 再次筛选入度为0的顶点
#     return Seq
