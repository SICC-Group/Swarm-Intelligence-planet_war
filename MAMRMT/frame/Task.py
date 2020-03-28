import pygame
class Task:
    def __init__(self,taskId,priority,status,target):
        self.taskId=taskId
        self.priority=priority
        self.status=status
        self.target=target

    def updateStatus(self,status):
        self.status=status


class ObserveTask(Task):
    def doTask(self,agent_obs,enemies):
        obs_emy=[]
        for enemy in enemies.sprites():
            if (agent_obs.contains(enemy.rect)):
                obs_emy.append((enemy.rect[0],enemy.rect[1]))
        return obs_emy

class AttrackTask(Task):
    def doTask(self):
        pass






