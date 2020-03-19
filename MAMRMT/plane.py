import pygame
import random
import time
import os.path
from datetime import datetime
from pygame.locals import *  # import pygame.locals for easier access to key coordinates
from pygame.font import *  # import font
import ast
from MAMRMT.role import *
# from MAMRMT.frame import *


def show_text(surface_handle, pos, text, color, font_bold=False, font_size=13, font_italic=False):
    cur_font = pygame.font.SysFont("宋体", font_size)  # 获取系统字体，并设置文字大小
    cur_font.set_bold(font_bold)  # 设置是否加粗属性
    cur_font.set_italic(font_italic)  # 设置是否斜体属性
    text_fmt = cur_font.render(text, 1, color)  # 设置文字内容
    surface_handle.blit(text_fmt, pos)  # 绘制文字


def select_action(enemy_x, exeAgent1_x, exeAgent2_x):
    ac1 = 0
    ac2 = 0
    gap1 = abs(enemy_x - exeAgent1_x)
    gap2 = abs(enemy_x - exeAgent2_x)
    if gap1 <= gap2:
        if enemy_x > exeAgent1_x:
            ac1 = 4
        elif enemy_x < exeAgent1_x:
            ac1 = 3
        else:
            ac1 = 0
    else:
        if enemy_x > exeAgent2_x:
            ac2 = 4
        elif enemy_x < exeAgent2_x:
            ac2 = 3
        else:
            ac2 = 0
    return ac1, ac2


def playGame():
    pygame.init()  # initialize pygame
    screen = pygame.display.set_mode((width, hight))  # create the screen object
    # 创建游戏背景
    background = pygame.Surface(screen.get_size())
    background.fill((135, 206, 250))
    # Create a custom event for adding a new enemy.
    # 自定义事件 每隔500ms触发增加enemy
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 250)
    ADDCLOUD =pygame.USEREVENT + 2
    pygame.time.set_timer(ADDCLOUD, 1000)
    ADDBULLET = pygame.USEREVENT + 3
    pygame.time.set_timer(ADDBULLET, 100)
    # 创建player
    player = ManageAgent_pw(0)
    player2 = ManageAgent_pw(1)
    player3 = ManageAgent_pw(2)
    Player_list = [player, player2, player3]
    # 分配管理agent和执行agent
    index = random.randint(0, 2)
    mngAgent = ManageAgent_pw(Player_list[index].roleId)
    exeAgent1 = ExecuteAgent_pw(Player_list[index - 1].roleId)
    exeAgent2 = ExecuteAgent_pw(Player_list[index - 2].roleId)

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
    task_diagram = cfg['task']['task_diagram']
    task_diagram_seq = ast.literal_eval(task_diagram)   # 将字符串转为字典
    task_lt = taskOrder(task_diagram_seq)
    print(task_lt)
    mngAgent.composeTask(mngAgent.divideTask(task_lt)[0], 0, '未完成', 0)
    exeAgent1.composeTask(mngAgent.divideTask(task_lt)[1], 0, '未完成', 1)
    exeAgent2.composeTask(mngAgent.divideTask(task_lt)[2], 0, '未完成', 1)

    # exeAgent1.executeTask(0)
    # exeAgent2.executeTask(1)
    # main loop
    flag = False
    life1 = 10
    life2 = 10
    life3 = 10
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
                enemy = new_enemy.get_pos()
                flag = True
            elif event.type == ADDCLOUD:
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)
            elif event.type == ADDBULLET:
                if (len(bullets) <= 6) and (game_over == False):
                    # 攻击机发射子弹
                    new_bullet = Bullet(exeAgent1.rect[0] + 32, exeAgent1.rect[1])
                    bullets.add(new_bullet)
                    all_sprites.add(new_bullet)
                    new_bullet2 = Bullet(exeAgent2.rect[0] + 32, exeAgent2.rect[1])
                    bullets.add(new_bullet2)
                    all_sprites.add(new_bullet2)

        clouds.update()
        enemies.update()
        # 获取智能体的位置
        pos = mngAgent.get_pos()
        pos1 = exeAgent1.get_pos()
        pos2 = exeAgent2.get_pos()
        if game_over == False:
            # 随机选择动作移动
            # action = random.randint(0, 4)
            # exeAgent1.update(action)
            # action2 = random.randint(0, 4)
            # exeAgent2.update(action2)
            action3 = random.randint(0, 4)
            mngAgent.update(action3)
            if flag == True:
                action = select_action(enemy[0],pos1[0],pos2[0])
                exeAgent1.update(action[0])
                exeAgent2.update(action[1])

        bullets.update()
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
        # 遇到敌人，在原位置初始化
        if pygame.sprite.spritecollideany(exeAgent1, enemies):
            life1 = life1 - 3
            exeAgent1.__init__(0)
        if pygame.sprite.spritecollideany(exeAgent2, enemies):
            life2 = life2 - 3
            exeAgent2.__init__(1)
        if pygame.sprite.spritecollideany(mngAgent, enemies):
            life3 = life3 - 3
            mngAgent.__init__(2)
        # 击中敌人
        if pygame.sprite.groupcollide(bullets, enemies, True, True):
            player_hit_enemies += 1
            if player_hit_enemies >= 50:
                if life1 > 0:
                    exeAgent1.task.updateStatus('完成')
                if life2 > 0:
                    exeAgent2.task.updateStatus('完成')
                print('exeAgent1的任务编号：', exeAgent1.task.taskId, '状态：', exeAgent1.task.status)
                print('exeAgent2的任务编号：', exeAgent2.task.taskId, '状态：', exeAgent2.task.status)
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
        # mngAgent1_life = u"mngAgent life:%d" % life3
        show_text(screen, (20, 20), score_text, (0, 0, 255), False, font_size=28)
        show_text(screen, (20, 40), game_time, (0, 0, 255), False, font_size=28)
        show_text(screen, (20, 60), 'MngAgent:1 ExeAgent:2', (0, 0, 255), False, font_size=28)
        # show_text(screen, (20, 80), mngAgent1_life, (0, 0, 255), False, font_size=28)
        pygame.display.flip()

if __name__ == "__main__":
    # 定义游戏的屏幕大小
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    playGame()
