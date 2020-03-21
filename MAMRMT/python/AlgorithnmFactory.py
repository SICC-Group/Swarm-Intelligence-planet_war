from python.Role import *
#抽象工厂
class AgentFactory:
    def createManager(self,roleId):
        pass

    def createExecute(self,roleId):
        pass

#合同网工厂
class ContractNetFactory(AgentFactory):
    def createManager(self,roleId):
        return ManagerContractNet(roleId);

    def createExecute(self,roleId):
        return ExecuteContractNet(roleId);

#遗传算法工厂
class GeneticFactory(AgentFactory):
    def createManager(self,roleId):
        return ManagerGenetic(roleId);

    def createExecute(self,roleId):
        return ExecuteGenetic(roleId);

#DQN工厂
class DQNFactory(AgentFactory):
    def createManager(self,roleId):
        return ManagerDQN(roleId);

    def createExecute(self,roleId):
        return ExecuteDQN(roleId);
