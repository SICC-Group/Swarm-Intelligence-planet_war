# import json
# class Field():
#     def __init__(self, n_role):
#         # 战场
#         self.field_width = 600
#         self.field_length = 800
#         self.role1 = "打击"
#         self.role2 = "侦查"
#
#         # plane
#         self.n_plane = 2
#         self.observation_size = 10  # 我方飞机观测范围10*10
#         self.n_role = n_role
#         self.n_action = 5  # 0:STILL, 1:MOVE_NORTH, 2:MOVE_EAST, 3:MOVE_SOUTH, 4:MOVE_WEST
#         self.life = 20
#         self.n_bullet = 100
#         # enemy
#         self.n_enemy = 100
#         self.enemy_speed = 3
#         self.enemy_life = 10
#         self.init_position = [10, 100, 200, 300, 400, 500, 600, 700, 790]
#         # bullet
#         self.bullet_seed = 1
#
#         ini_info = {"field": {"field_width": 600, "field_length": 800},
#                     "role": {"n_role": 2,"role1_agentID": 0,"role2_agentID": "[1,2]"},
#                     "task": {"general_task": 1,"n_task": 5,
#                         "task_diagram": "['1':'234','2':'5','3':'25','4':'35','5':'']"},
#                     "agent": {
#                         "plane": {"n_plane": 2, "observation_size": 10, "n_role": n_role, "n_action": 5, "life": 20,
#                                   "n_bullet": 100},
#                         "enemy": {"n_enemy": 100, "enemy_speed": 3, "enemy_life ": 10},
#                         "bullet": {"bullet_seed": 1}
#                     }
#                     }
#         msg = {"field": {"field_width": 600, "field_length": 800},
#                "role": {"n_role": n_role, self.role1: 1, self.role2: 1},
#                "task": {self.role1: "observation", self.role2: "transportation"},
#                "agent": {
#                    "enemy": {"now_enemy": 10, "pos": "(10,10),(20,100),30,40,50,10,20,30,(80,80)"},
#                    "plane1": {
#                        "pos": "(100, 100)",
#                        "manager_agent": True,
#                        "mana_task": "接受任务/划分任务/发布任务/分配任务/接受反馈结果",
#                        "role_id": 1,
#                        "task": "fire",
#                        "next_action": 2,  # 2 为右移
#                        "enemy_pos": "(90,90)",
#                        "life": 28
#                    },
#                    "plane2": {
#                        "pos": "(200,200)",
#                        "manager_agent": False,
#                        "role_id": 2,
#                        "task": "observation",
#                        "complete": 8,
#                        "next_action": 5,  # 5为侦查
#                        "enemy_pos": "(10,10),(20,100),30,40,50,10,20,30,(80,80)",
#                        "life": 15
#                    }
#                }
#
#                }
#
#         json_info = json.dumps(ini_info,indent=4,ensure_ascii=False)
#         # data = open("FieldInfo_ini.txt","w")
#         # data.write(json_info)
#         # data.close()
#         print(json_info)
#         # json_info2 = json.dumps(msg, indent=4, ensure_ascii=False)
#         # data2 = open("msg.txt", "w")
#         # data2.write(json_info2)
#         # data2.close()
#         # print(json_info2)
#
#
# if __name__ == "__main__":
#     field = Field(2)
# l = []
# x= 1
# y =2
# l.append(x)
# l.append(y)
# init_position = [[10,10], 100, 200, 300, 400, 500, 600, 700, 790]
# init_position.append(l)
# print(init_position)
