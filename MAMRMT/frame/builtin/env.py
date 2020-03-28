import pygame
import random
import os.path
from datetime import datetime
from MAMRMT.frame.builtin.built import *
from MAMRMT.frame.Test import *
from MAMRMT.frame.Task import *

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
        pygame.time.set_timer(self.ADDENEMY, 600)
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
        # 初始化参数
        self.start_time = datetime.now()
        self.enemy_num = 0
        self.player_hit_enemies = 0

    def updateEnv(self,mngAgent,agent):
        self.all_sprites.add(mngAgent)
        for exeAgent in agent.values():
            self.all_sprites.add(exeAgent)

    def get_observation(self,mngAgent,agent):
        self.screen.blit(self.background, (0, 0))
        for event in pygame.event.get():
            # 结束游戏
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
            elif event.type == QUIT:
                return False
            # 敌机
            if event.type == self.ADDENEMY:
                self.enemy_num +=1
                new_enemy = Enemy(self.size, self.enemy_num)
                self.enemies.add(new_enemy)
                self.all_sprites.add(new_enemy)
            # 云朵
            elif event.type == self.ADDCLOUD:
                new_cloud = Cloud(self.size)
                self.clouds.add(new_cloud)
                self.all_sprites.add(new_cloud)
            # 子弹
            elif event.type == self.ADDBULLET:
                if (len(self.bullets) <= 3):
                    # 发射子弹
                    for exeAgent in agent.values():
                        new_bullet = Bullet(exeAgent.rect[0] + 32, exeAgent.rect[1])
                        self.bullets.add(new_bullet)
                        self.all_sprites.add(new_bullet)
        self.clouds.update()
        self.enemies.update()
        # emy_pos记录当前页面的敌机位置
        emy_pos = {}
        for enemy in self.enemies.sprites():
            emy_pos[enemy.id]=(enemy.rect[0],enemy.rect[1])
        print("敌机位置：", emy_pos)
        # agent_pos记录agent位置
        agent_pos = {}
        agent_pos["m"] = (mngAgent.rect[0],mngAgent.rect[1])
        mngAgent.update(0, 0)
        # 观测范围
        task = ObserveTask(0, 0, 0, 0)
        obs_emy=mngAgent.doTask(task,self.enemies)
        for exeAgent in agent.values():
            # exeAgent位置
            agent_pos[exeAgent.roleId] =(exeAgent.rect[0],exeAgent.rect[1])
            obs_emy+=exeAgent.doTask(task,self.enemies)
        print("agent位置：", agent_pos)
        obs_emy=list(set(obs_emy))
        print("联合观测范围：",obs_emy)
        print("\n\n")
        return agent_pos,obs_emy

    def get_hitEnemies(self):
        self.bullets.update()
        for entity in self.all_sprites:
            self.screen.blit(entity.image, entity.rect)
            # 击中敌人
            if pygame.sprite.groupcollide(self.bullets, self.enemies, True, True):
                self.player_hit_enemies += 1
        return self.player_hit_enemies

    def getScore(self,agent):
        current_time = datetime.now()
        total_time = (current_time -self.start_time).seconds
        # 分数显示
        score_text = u"Score: %s" % self.player_hit_enemies
        game_time = u"Game time:%ds" % total_time
        show_text(self.screen, (20, 20), score_text, (0, 0, 255), False, font_size=28)
        show_text(self.screen, (20, 40), game_time, (0, 0, 255), False, font_size=28)
        show_text(self.screen, (20, 60), 'MngAgent:1 ExeAgent:' + str(len(agent)), (0, 0, 255), False, font_size=28)

def show_text(surface_handle, pos, text, color, font_bold=False, font_size=13, font_italic=False):
    cur_font = pygame.font.SysFont("宋体", font_size)  # 获取系统字体，并设置文字大小
    cur_font.set_bold(font_bold)  # 设置是否加粗属性
    cur_font.set_italic(font_italic)  # 设置是否斜体属性
    text_fmt = cur_font.render(text, 1, color)  # 设置文字内容
    surface_handle.blit(text_fmt, pos)  # 绘制文字







