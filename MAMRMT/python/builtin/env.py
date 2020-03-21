import pygame
import random
import os.path
from datetime import datetime
from python.builtin.built import *
from python.Test import *

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
        pygame.time.set_timer(self.ADDENEMY, 1000)
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
        pygame.display.flip()
        # 初始化参数
        start_time = datetime.now()
        player_hit_enemies = 0
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
                # 敌机
                elif event.type == self.ADDENEMY:
                    new_enemy = Enemy(self.size)
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
            #敌机位置
            for enemy in self.enemies.sprites():
                print(enemy.rect)
            e1_obs = pygame.Rect(0, 0, 0, 0)
            e2_obs = pygame.Rect(0, 0, 0, 0)
            m_obs = pygame.Rect(0, 0, 0, 0)

            if game_over == False:
                # 随机选择动作移动
                for exeAgent in agent.values():
                    action = random.randint(0, 4)
                    exeAgent.update(action,self.size)
                    print(exeAgent.rect)
                    # exeAgent位置
                    e1_obs = exeAgent.rect.copy()
                    # 原位置放大后的矩形
                    e1_obs.inflate_ip(30, 30)
                action1= random.randint(0, 4)
                mngAgent.update(action1,self.size)
                for enemy in self.enemies.sprites():
                    if (enemy.rect[0] > 0) & (enemy.rect[1] > 0):
                        print(enemy.rect)
                        if (enemy.rect[0] >= e1_obs[0]) & (enemy.rect[1] >= e1_obs[1]) & (
                                enemy.rect[0] + 32 <= e1_obs[0] + 94) & (enemy.rect[1] + 32 <= e1_obs[1] + 94):
                            print("e1观测到敌机位置：")
                            print(enemy.rect)
                        else:
                            print("None")
                        if (enemy.rect[0] >= e2_obs[0]) & (enemy.rect[1] >= e2_obs[1]) & (
                                enemy.rect[0] + 32 <= e2_obs[0] + 94) & (enemy.rect[1] + 32 <= e2_obs[1] + 94):
                            print("e2观测到敌机位置：")
                            print(enemy.rect)
                        else:
                            print("None")
                        if (enemy.rect[0] >= m_obs[0]) & (enemy.rect[1] >= m_obs[1]) & (
                                enemy.rect[0] + 32 <= m_obs[0] + 164) & (enemy.rect[1] + 32 <= m_obs[1] + 164):
                            print("m观测到敌机位置：")
                            print(enemy.rect)
                        else:
                            print("None")
            self.bullets.update()
            for entity in self.all_sprites:
                self.screen.blit(entity.image, entity.rect)

            # 击中敌人
            if pygame.sprite.groupcollide(self.bullets, self.enemies, True, True):
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






