class blackboard:
    def __init__(self):
        self.observe=[]

    def register(self,role):
        self.observe.append(role)

    def unregister(self,role):
        self.observe.remove(role)

    #一对多通信
    def notify(self,task):
        for exeAgent in self.observe:
            exeAgent.execute(task[exeAgent.roleId], 2)




