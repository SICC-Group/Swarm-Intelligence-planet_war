class Task:
    '''
        task编号
        优先级
        状态
        最晚开始时间
        预估执行时间
        目标
    '''
    def __init__(self,taskId,priority,status,startTime,executeTime,target):
        self.taskId=taskId
        self.priority=priority
        self.status=status
        self.startTime=startTime
        self.executeTime=executeTime
        self.target=target

    def updateStatus(self,status):
        self.status=status

