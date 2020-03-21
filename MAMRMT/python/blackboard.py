class blackboard:
    def __init__(self):
        self.observe=[]

    def register(self,role):
        self.observe.append(role)

    def unregister(self,role):
        self.observe.remove(role)

    '一对多通信'
    def notify(self):
        for role in self.observe:
            role.execute()

    '一对一通信'
    def one(self,role):
        role.execute()




