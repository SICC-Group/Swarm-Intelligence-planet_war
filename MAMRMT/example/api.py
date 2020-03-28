from MAMRMT.frame.builtin.env import *
from MAMRMT.frame.Test import *
from frame.blackboard import *
import pygame

if __name__ == "__main__":
    # init the game
    env = environment(800, 600)
    # init models
    test = Test(ContractNetFactory())
    # init env and agents
    list = [1, 2, 3]
    index = random.randint(1,3)
    mngAgent = test.getManager(index)
    agent={}
    exeAgent1 = test.getExecute(list[index - 1])
    agent[list[index - 1]]=exeAgent1
    exeAgent2 = test.getExecute(list[index - 2])
    agent[list[index - 2]]=exeAgent2
    env.updateEnv(mngAgent,agent)
    # init blackboard
    blackboard=blackboard()
    blackboard.register(exeAgent1)
    blackboard.register(exeAgent2)
    # main loop
    running=True
    while running:
        #get observation
        data=env.get_observation(mngAgent,agent)
        if data==False:
            break
        else:
           task=mngAgent.assignTask(data)
           # set action
           blackboard.notify(task)
           # get score
           env.getScore(agent)
        if(env.get_hitEnemies()>50):
            break
        pygame.display.flip()


