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
'''
managerId=random.randint(1,4)
test=Test(ContractNetFactory())
agent={}
execute_list=[]
for i in range(1,5):
    if(i==managerId):
        manager=test.getManager(i)
        agent[i]=manager
    else:
        execute_list.append(i)
        agent[i]=test.getExecute(i)
graph={'1':'234','2':'5','3':'25','4':'35','5':''}
task_list=manager.taskOrder(graph)
if(len(task_list)==len(graph)):
    data=manager.acceptTask(task_list,execute_list)
    blackboard=blackboard()
    blackboard.one(agent[data])
    blackboard.register(agent[3])
    blackboard.register(agent[4])
    blackboard.notify()
else:
    print("there is a circle.")
'''


