import pygame
import random
import time
import os.path
from datetime import datetime
from pygame.locals import *  # import pygame.locals for easier access to key coordinates
from pygame.font import *  # import font

from MAMRMT.role import *

width = 800
hight = 600


def show_text(surface_handle, pos, text, color, font_bold=False, font_size=13, font_italic=False):
    cur_font = pygame.font.SysFont("宋体", font_size)  # 获取系统字体，并设置文字大小
    cur_font.set_bold(font_bold)  # 设置是否加粗属性
    cur_font.set_italic(font_italic)  # 设置是否斜体属性
    text_fmt = cur_font.render(text, 1, color)  # 设置文字内容
    surface_handle.blit(text_fmt, pos)  # 绘制文字


def get_observation(agent):
    pass


def playGame():
    pygame.init()  # initialize pygame
    screen = pygame.display.set_mode((width, hight))  # create the screen object
    # 创建游戏背景
    background = pygame.Surface(screen.get_size())
    background.fill((135, 206, 250))
    # Create a custom event for adding a new enemy.
    # 自定义事件 每隔300ms触发增加enemy
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 1000)
    ADDCLOUD = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDCLOUD, 1000)
    ADDBULLET = pygame.USEREVENT + 3
    pygame.time.set_timer(ADDBULLET, 100)

    # 创建player
    player = Player(0)
    player2 = Player(1)
    player3 = Player(2)
    Player_list = [player, player2, player3]
    # 分配管理agent和执行agent
    index = random.randint(0, 2)
    mngAgent = ManageAgent(Player_list[index].roleId)
    exeAgent1 = ExecuteAgent(Player_list[index - 1].roleId)
    exeAgent2 = ExecuteAgent(Player_list[index - 2].roleId)

    enemies = pygame.sprite.Group()       # 创建敌人集合
    clouds = pygame.sprite.Group()        # 创建云彩集合
    bullets = pygame.sprite.Group()       # 创建子弹集合
    all_sprites = pygame.sprite.Group()   # 创建agent集合
    all_sprites.add(exeAgent1)
    all_sprites.add(exeAgent2)
    all_sprites.add(mngAgent)

    # 初始化参数
    start_time = datetime.now()
    current_time = start_time
    player_hit_enemies = 0
    pygame.display.flip()
    running = True
    game_over = False
    # 任务初始化
    # -----
    exeAgent1.composeTask(0, 0, '未完成')
    exeAgent2.composeTask(1, 0, '未完成')
    # exeAgent1.executeTask(0)
    # exeAgent2.executeTask(1)
    # main loop
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False  # 结束游戏
            elif event.type == QUIT:
                running = False
            elif event.type == ADDENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type == ADDCLOUD:
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)
            elif event.type == ADDBULLET:
                if (len(bullets) <= 3) and (game_over == False):
                    # 攻击机发射子弹
                    new_bullet = Bullet(exeAgent1.rect[0] + 32, exeAgent1.rect[1])
                    bullets.add(new_bullet)
                    all_sprites.add(new_bullet)
                    new_bullet2 = Bullet(exeAgent2.rect[0] + 32, exeAgent2.rect[1])
                    bullets.add(new_bullet2)
                    all_sprites.add(new_bullet2)

        clouds.update()
        enemies.update()
        # e_pos 记录当前页面的敌机位置
        e_pos = []
        for enemy in enemies.sprites():
        #     tmp = []
        #     e_x = enemy.rect[0]
        #     e_y = enemy.rect[1]
        #     if e_y > 0:
        #         tmp.append(e_x)
        #         tmp.append(e_y)
        #         e_pos.append(tmp)
        # print("敌机位置")
        # print(e_pos)
            print(enemy.rect)
        e1_obs = pygame.Rect(0, 0, 0, 0)
        e2_obs = pygame.Rect(0, 0, 0, 0)
        m_obs = pygame.Rect(0, 0, 0, 0)

        if game_over == False:
            # 随机选择动作移动
            action = random.randint(0, 4)
            exeAgent1.update(action)
            print("e1:")
            print(exeAgent1.rect)
            e1_obs = exeAgent1.rect.copy()
            print("e1_obs_copy:")
            print(e1_obs)
            e1_obs.inflate_ip(30, 30) # 原位置放大后的矩形
            # exeAgent1.rect.inflate_ip(20,20)
            print("e1_obs:")
            print(e1_obs)
            # x1,y1 = exeAgent1.rect[0][1]
            action2 = random.randint(0, 4)
            exeAgent2.update(action2)
            e2_obs = exeAgent2.rect.copy()
            e2_obs.inflate_ip(30, 30)
            print("e2_obs:")
            print(e2_obs)
            action3 = random.randint(0, 4)
            mngAgent.update(action3)
            m_obs = exeAgent1.rect.copy()
            m_obs.inflate_ip(100,100)
            print("m_obs:")
            print(m_obs)
            for enemy in enemies.sprites():
                if (enemy.rect[1] > 0)&(enemy.rect[1] > 0):
                    print(enemy.rect)
                    if (enemy.rect[0]>=e1_obs[0])&(enemy.rect[1]>=e1_obs[1])&(enemy.rect[0]+32<=e1_obs[0]+94)&(enemy.rect[1]+32<=e1_obs[1]+94):
                        print("e1观测到敌机位置：")
                        print(enemy.rect)
                    else:
                        print("None")
                    if (enemy.rect[0] >= e2_obs[0]) & (enemy.rect[1] >= e2_obs[1])&(enemy.rect[0]+32<=e2_obs[0]+94)&(enemy.rect[1]+32<=e2_obs[1]+94):
                        print("e2观测到敌机位置：")
                        print(enemy.rect)
                    else:
                        print("None")
                    if (enemy.rect[0] >= m_obs[0]) & (enemy.rect[1] >= m_obs[1])&(enemy.rect[0]+32<=m_obs[0]+164)&(enemy.rect[1]+32<=m_obs[1]+164):
                        print("m观测到敌机位置：")
                        print(enemy.rect)
                    else:
                        print("None")
                    # flag1 = e1_obs.contains(enemy.rect)
                    # if flag1 == 1:
                    #     print("e1观测到敌机位置：")
                    #     print(enemy.rect)
                    # else:
                    #     print("None")
                    # flag2 = e2_obs.contains(enemy.rect)
                    # if flag1 == 1:
                    #     print("e2观测到敌机位置：")
                    #     print(enemy.rect)
                    # else:
                    #     print("None")
                    # flag3 = m_obs.contains(enemy.rect)
                    # if flag1 == 1:
                    #     print("m观测到敌机位置：")
                    #     print(enemy.rect)
                    # else:
                    #     print("None")



        # 判断观测范围内的敌机位置
        # obs_enemy = pygame.Rect(0, 0, 0, 0)
        obs1_enemy_pos = []
        obs2_enemy_pos = []
        obs3_enemy_pos = []
        # for enemy in enemies.sprites():
        #     # print(enemy.rect)
        #     # obs1_enemy = pygame.Rect(0, 0, 0, 0)
        #     # obs2_enemy = pygame.Rect(0, 0, 0, 0)
        #     # obs3_enemy = pygame.Rect(0, 0, 0, 0)
        #     if enemy.rect[1] > 0:
        #         print("enemy")
        #         print(enemy.rect)
        #         flag = e1_obs.contains(enemy.rect)
        #         if flag == True:
        #             print("观测到敌机位置：")
        #             print(enemy.rect)
        #         else:
        #             print("无敌机信息")
        #         tmp2 = []
        #         tmp2.append(obs1_enemy.x)
        #         tmp2.append(obs1_enemy.y)
        #         obs1_enemy_pos.append(tmp2)
        #         print(obs1_enemy_pos)
        #         obs2_enemy = e2_obs.clip(enemy.rect)
        #         tmp2 = []
        #         tmp2.append(obs2_enemy.x)
        #         tmp2.append(obs2_enemy.y)
        #         obs2_enemy_pos.append(tmp2)
        #         print(obs2_enemy_pos)
        #         obs3_enemy = m_obs.clip(enemy.rect)
        #         tmp2 = []
        #         tmp2.append(obs3_enemy.x)
        #         tmp2.append(obs3_enemy.y)
        #         obs3_enemy_pos.append(tmp2)
        #         print(obs3_enemy_pos)
        # # print(obs1_enemy_pos,obs2_enemy_pos,obs3_enemy_pos)

        bullets.update()
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)

        # 遇到敌人，在原位置初始化
        # if pygame.sprite.spritecollideany(exeAgent1, enemies):
        #     exeAgent1.__init__(0)
        # if pygame.sprite.spritecollideany(exeAgent2, enemies):
        #     exeAgent2.__init__(1)
        # if pygame.sprite.spritecollideany(mngAgent, enemies):
        #     mngAgent.__init__(2)
        # 击中敌人
        if pygame.sprite.groupcollide(bullets, enemies, True, True):
            player_hit_enemies += 1
            if player_hit_enemies >= 50:
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
        show_text(screen, (20, 20), score_text, (0, 0, 255), False, font_size=28)
        show_text(screen, (20, 40), game_time, (0, 0, 255), False, font_size=28)
        show_text(screen, (20, 60), 'MngAgent:1 ExeAgent:2', (0, 0, 255), False, font_size=28)
        pygame.display.flip()


if __name__ == "__main__":
    # 定义游戏的屏幕大小
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    playGame()
