import json
'''
    Observation: (position of current agent, current goal, other agents, other goals, obstacles)
    战场100*100，agent可观测20*20，侦察时可观察100*100
    Action space: (Tuple)
        agent_id: positive integer
        action: {0:STILL, 1:MOVE_NORTH, 2:MOVE_EAST, 3:MOVE_SOUTH, 4:MOVE_WEST,
        5:FIRE, 6:, 7:SW, 8:NW}
    Reward: ACTION_COST for each action, GOAL_REWARD when robot arrives at target
'''
class Field():
    def __init__(self, n_role):
        # 战场
        self.field_width = 600
        self.field_length = 800
        # plane
        self.n_plane = 2
        self.observation_size = 10  # 我方飞机观测范围10*10
        self.n_role = n_role
        self.n_action = 5  # 0:STILL, 1:MOVE_NORTH, 2:MOVE_EAST, 3:MOVE_SOUTH, 4:MOVE_WEST
        self.life = 20
        self.n_bullet = 100
        # enemy
        self.n_enemy = 100
        self.enemy_speed = 3
        self.enemy_life = 10
        self.init_position = [10, 100, 200, 300, 400, 500, 600, 700, 790]
        # bullet
        self.bullet_seed = 1



    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self):
        info = {"field":{"field_width":600,"field_length":800},\
                "plane":{"n_plane":2,"observation_size":10,"n_role":n_role,"n_action":5 ,"life":20,"n_bullet":100},\
                "enemy":{"n_enemy":100,"enemy_speed":3,"enemy_life ":10},\
                "bullet":{"bullet_seed":1}
                }
        json_info = json.dumps(info,indent=4)
        # data = open("FieldInfo.txt","w")
        # data.write(json_info)
        # data.close()
        print(json_info)

    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None


# class ManageAgent(plane.palne):
#     pass
# class ExecuteAgent(plane.palne):
#     pass

if __name__ == "__main__":
    n_role = 2
    field = Field(n_role)
    field.render()




