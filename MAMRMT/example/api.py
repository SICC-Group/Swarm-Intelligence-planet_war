import random
from Swarm_Intelligence_planet_war.MAMRMT.frame.builtin.env import *
from Swarm_Intelligence_planet_war.MAMRMT.frame.Test import *
from Swarm_Intelligence_planet_war.MAMRMT.frame.environment import *
if __name__ == "__main__":
    # init the game
    env = environment(800, 600)
    # init models
    test = Test(ContractNetFactory())
    # init env and agents
    list = [0, 1, 2]
    index = random.randint(0, 2)
    mngAgent = test.getManager(index)
    agent={}
    exeAgent1 = test.getExecute(list[index - 1])
    agent[list[index - 1]]=exeAgent1
    exeAgent2 = test.getExecute(list[index - 2])
    agent[list[index - 2]]=exeAgent2
    env.updateEnv(mngAgent,agent)
    # get group handles

    # take action
    # simulate oe step
    # get reward
    # clear dead agents
    # reach max number of cycles
    pass