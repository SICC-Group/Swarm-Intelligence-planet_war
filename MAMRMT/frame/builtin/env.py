import pygame
import random
import os.path
from datetime import datetime
from Swarm_Intelligence_planet_war.MAMRMT.frame.builtin.built import *
from Swarm_Intelligence_planet_war.MAMRMT.frame.Test import *

class environment:

    def __init__(self,width,height):
        # 初始化
        pygame.init()
        # 屏幕对象
        self.size=(width,height)
        self.screen = pygame.display.set_mode(self.size)
        # 创建游戏背景
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((135, 206, 250))
        # 自定义事件(敌机、云朵、发射子弹)
        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, 900)
        self.ADDCLOUD = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADDCLOUD, 1000)
        self.ADDBULLET = pygame.USEREVENT + 3
        pygame.time.set_timer(self.ADDBULLET, 100)
        # 创建敌人集合
        self.enemies = pygame.sprite.Group()
        # 创建云彩集合
        self.clouds = pygame.sprite.Group()
        # 创建子弹集合
        self.bullets = pygame.sprite.Group()
        # 创建agent集合
        self.all_sprites = pygame.sprite.Group()

    def updateEnv(self,mngAgent,agent):
        self.all_sprites.add(mngAgent)
        for exeAgent in agent.values():
            self.all_sprites.add(exeAgent)
        # 执行agent初始坐标
        l = []
        for key in agent:
            l.append(key)
        agent[l[0]].rect.move_ip(600, 0)
        pygame.display.flip()
        # 初始化参数
        start_time = datetime.now()
        task_n = 50 # 总任务数
        player_hit_enemies = 0
        enemy_num = 0
        running = True
        game_over = False
        # main loop
        while running:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                # 结束游戏
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                # 结束游戏
                elif event.type == QUIT:
                    running = False
                # # 敌机
                elif event.type == self.ADDENEMY:
                    enemy_num += 1
                    new_enemy = Enemy(self.size)
                    new_enemy.id = enemy_num

                    self.enemies.add(new_enemy)
                    self.all_sprites.add(new_enemy)
                # 云朵
                elif event.type == self.ADDCLOUD:
                    new_cloud = Cloud(self.size)
                    self.clouds.add(new_cloud)
                    self.all_sprites.add(new_cloud)
                # 子弹
                elif event.type == self.ADDBULLET:
                    if (len(self.bullets) <= 3) and (game_over == False):
                        #发射子弹
                        for exeAgent in agent.values():
                            new_bullet = Bullet(exeAgent.rect[0] + 32,exeAgent.rect[1])
                            self.bullets.add(new_bullet)
                            self.all_sprites.add(new_bullet)
                        pass
            self.clouds.update()
            self.enemies.update()

            # e_pos 记录当前页面的敌机位置
            emy_pos = []
            emy_pos_dic = {}
            for enemy in self.enemies.sprites():
                # print("敌机编号：", enemy.id)
                # print("敌机位置：", get_pos(enemy))
                tmp = get_pos(enemy)
                emy_pos_dic[enemy.id] = tmp
                if len(tmp) > 0:
                    emy_pos.append(tmp)
            print("敌机位置列表：", emy_pos_dic)
            e1_obs = pygame.Rect(0, 0, 0, 0)
            e2_obs = pygame.Rect(0, 0, 0, 0)
            m_obs = pygame.Rect(0, 0, 0, 0)
            exeAgent_obs = [e1_obs, e2_obs]
            if game_over == False:
                agt_pos = []
                i = 0
                # 随机选择动作移动
                action = random.randint(0, 4)
                mngAgent.update(action, self.size)
                for exeAgent in agent.values():
                    # action = random.randint(0, 4)
                    # action = 0
                    # exeAgent.update(action, self.size)
                    tmp = get_pos(exeAgent)
                    agt_pos.append(tmp)
                    # exeAgent位置
                    exeAgent_obs[i] = exeAgent.rect.copy()
                    # 原位置放大后的矩形
                    # exeAgent_obs[i].inflate_ip(100, 200)
                    i += 1
                agt_pos.append(get_pos(mngAgent))
                print("执行a、管理a位置:",agt_pos)
                e1_obs = exeAgent_obs[0]
                e1_obs.inflate_ip(100, 200)
                e2_obs = exeAgent_obs[1]
                e2_obs.inflate_ip(100, 200)
                # print(e1_obs)
                # print(e2_obs)

                action1 = random.randint(0, 4)
                action1 = 0
                mngAgent.update(action1,self.size)
                m_pos = get_pos(mngAgent)
                agt_pos.append(m_pos)
                m_obs = mngAgent.rect.copy()
                m_obs.inflate_ip(400, 400)


                e1_emy = []
                e2_emy = []
                m_emy = []
                obs_emy = []  # 联合观测范围
                e1_task_id = []
                e2_task_id = []
                m_task_id = []
                obs_task = 0
                task_id = []  # 任务列表
                j = 0 # 记录敌机数量
                for enemy in self.enemies.sprites():
                    flag1 = e1_obs.contains(enemy.rect)
                    if flag1 == 1:
                        tmp = get_pos(enemy)
                        e1_emy.append(tmp)
                        e1_task_id.append(enemy.id)

                    flag2 = e2_obs.contains(enemy.rect)
                    if flag2 == 1:
                        tmp = get_pos(enemy)
                        e2_emy.append(tmp)
                        e2_task_id.append(enemy.id)

                    flag3 = m_obs.contains(enemy.rect)
                    if flag3 == 1:
                        tmp = get_pos(enemy)
                        m_emy.append(tmp)
                        m_task_id.append(enemy.id)

                print("e1观测到敌机位置：", e1_emy)
                print("e2观测到敌机位置：", e2_emy)
                print("m观测到敌机位置：", m_emy)
                obs_emy = (e1_emy + e2_emy + m_emy)
                print("联合观测范围：", obs_emy)
                task_id = [0]+e1_task_id + e2_task_id + m_task_id
                j = 0
                for enemy in self.enemies.sprites():
                    j += 1
                    if j % 5 == 0:
                        task_id.append(0)
                print("敌机任务列表：", task_id)
                att_task, obs_task = mngAgent.divideTask(task_id)
                print("攻击任务：",att_task)
                print("观测任务：",obs_task)
                todo_list = mngAgent.assignTask(agt_pos, att_task, obs_task, emy_pos_dic)
                print("任务分配：",todo_list)

                print("")
                print("")
                if len(att_task) > 0:
                    e1_atk = []
                    for exeAt1 in todo_list[1]:
                        enemy_id = exeAt1.target
                        e1_atk.append(enemy_id)
                    e2_atk = []
                    for exeAt2 in todo_list[2]:
                        enemy_id = exeAt2.target
                        e2_atk.append(enemy_id)
                    at_list =[e1_atk,e2_atk]
                    i = 0
                    for exeAgent in agent.values():
                        print('exeAgent:',exeAgent,'i:',i)
                        if len(at_list[i]) > 0:
                            act = exeAgent.execute(exeAgent.rect, at_list[i], emy_pos_dic)
                            exeAgent.update(act, self.size)
                        else:
                            i += 1
                            continue
                        i += 1
            self.bullets.update()
            for entity in self.all_sprites:
                self.screen.blit(entity.image, entity.rect)

            # 击中敌人

            if pygame.sprite.groupcollide(self.bullets, self.enemies, True, True):
                player_hit_enemies += 1
                task_undo = task_n - player_hit_enemies
                # 管理a接收任务
                task_undo = mngAgent.receiveTask(task_undo)
                if player_hit_enemies >= task_n:
                    game_over = True

            # 游戏结束，屏幕显示
            if game_over == True:
                break
            if game_over == False:
                current_time = datetime.now()
            total_time = (current_time - start_time).seconds
            # 分数显示
            score_text = u"Score: %s" % player_hit_enemies
            game_time = u"Game time:%ds" % total_time
            show_text(self.screen, (20, 20), score_text, (0, 0, 255), False, font_size=28)
            show_text(self.screen, (20, 40), game_time, (0, 0, 255), False, font_size=28)
            show_text(self.screen, (20, 60), 'MngAgent:1 ExeAgent'+str(len(agent)), (0, 0, 255), False, font_size=28)
            pygame.display.flip()



    def get_observation(self, handle):
        pass

    def set_action(self,action):
        pass

def show_text(surface_handle, pos, text, color, font_bold=False, font_size=13, font_italic=False):
    cur_font = pygame.font.SysFont("宋体", font_size)  # 获取系统字体，并设置文字大小
    cur_font.set_bold(font_bold)  # 设置是否加粗属性
    cur_font.set_italic(font_italic)  # 设置是否斜体属性
    text_fmt = cur_font.render(text, 1, color)  # 设置文字内容
    surface_handle.blit(text_fmt, pos)  # 绘制文字


def get_pos(agent):
    tmp = []
    x = agent.rect[0]
    y = agent.rect[1]
    tmp.append(x)
    tmp.append(y)
    return tmp




