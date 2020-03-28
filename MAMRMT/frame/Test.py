from MAMRMT.frame.AlgorithnmFactory import *
import random
import MAMRMT.frame.blackboard

class Test:
    def __init__(self,factory):
        self.factory=factory

    def getManager(self,roleId):
        agent=self.factory.createManager(roleId)
        return agent

    def getExecute(self,roleId):
        agent=self.factory.createExecute(roleId)
        return agent


