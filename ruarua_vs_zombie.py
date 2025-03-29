import pygame  # 导入游戏开发库
import sys     # 系统相关功能模块
import random  # 随机数生成模块
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = BASE_DIR

    return os.path.join(base_path, relative_path)

pygame.init() # 初始化pygame引擎
bgm = pygame.mixer.Sound(resource_path("src/music.mp3"))
loseend=0
winend=0
running=1
# 游戏窗口配置
SCREEN_WIDTH = 1080  # 屏幕宽度
SCREEN_HEIGHT = 720  # 屏幕高度
FPS = 60             # 帧率设置

class SunCounter:  # 阳光计数器类
    def __init__(self):
        self.sun = 100             # 初始阳光值
        self.last_update = pygame.time.get_ticks()  # 最后更新时间戳
        self.interval = 1000       # 阳光生成间隔（毫秒）

    def update(self):  # 定时增加阳光
        now = pygame.time.get_ticks()
        if now - self.last_update > self.interval:
            self.sun += 25
            self.last_update = now


class Player(pygame.sprite.Sprite):  # 玩家角色类
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(resource_path("src/rua.png")).convert_alpha()  # 加载角色贴图
        self.rect = self.image.get_rect(topleft=(65, 120))  # 初始位置

    def move_y(self, dy):  # 垂直移动控制
        new_y = self.rect.y + dy
        if -100 <= new_y <= 510: # 移动范围限制
            self.rect.y = new_y

    def move_x(self, dx):  # 水平移动控制
        new_x = self.rect.x + dx
        if 0 <= new_x <= 900: # 移动范围限制
            self.rect.x = new_x
            
            
class Zombie(pygame.sprite.Sprite):  # 僵尸类
    def __init__(self, y_pos):
        super().__init__()
        self.image = pygame.image.load(resource_path("src/zombie.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(1080, y_pos))  # 从右侧生成
        self.x = 1080.0  # 使用浮点数表示x位置
        self.speed = 0.9        # 移动速度
        self.active = True      # 存活状态

    def update(self):  # 僵尸移动逻辑
        if self.active:
            self.x -= self.speed
            self.rect.x = int(self.x)
            if self.rect.right < 0:  # 移出屏幕时失效
                self.kill()
                bgm.stop()
                pygame.mixer.Sound(resource_path("src/end.mp3")).play()
                pygame.mixer.Sound(resource_path("src/end2.mp3")).play()
                global loseend
                global running
                running = False
                loseend = 1

class YJH(pygame.sprite.Sprite):  # 僵尸类
    def __init__(self, y_pos):
        super().__init__()
        self.image = pygame.image.load(resource_path("src/yjh.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(0, y_pos))  # 从右侧生成
        self.x = 0.0  # 使用浮点数表示x位置
        self.speed = 0.5        # 移动速度
        self.active = True      # 存活状态
        self.hp = 70

    def update(self):  # 僵尸移动逻辑
        if self.active:
            self.x += self.speed
            self.rect.x = int(self.x)
            if self.rect.right > 1080:  # 移出屏幕时失效
                self.kill()
               

class ZZS(pygame.sprite.Sprite):  # 僵尸类
    def __init__(self, y_pos):
        super().__init__()
        self.image = pygame.image.load(resource_path("src/zzs2.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(1080, 90))  # 从右侧生成
        self.x = 1080.0  # 使用浮点数表示x位置
        self.speed = 0.7        # 移动速度
        self.active = True      # 存活状态
        self.hp = 120

    def update(self):  # 僵尸移动逻辑
        if self.active:
            self.x -= self.speed
            self.rect.x = int(self.x)
            if self.rect.right < 0:  # 移出屏幕时失效
                self.kill()
                bgm.stop()
                pygame.mixer.Sound(resource_path("src/end.mp3")).play()
                pygame.mixer.Sound(resource_path("src/end2.mp3")).play()
                global loseend
                global running
                running = False
                loseend = 1

class XGF(pygame.sprite.Sprite):  # 僵尸类
    def __init__(self, y_pos):
        super().__init__()
        self.image = pygame.image.load(resource_path("src/xgf.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(1080, y_pos))  # 从右侧生成
        self.x = 1080.0  # 使用浮点数表示x位置
        self.speed = 8        # 移动速度
        self.active = True      # 存活状态
        self.hp = 10

    def update(self):  # 僵尸移动逻辑
        if self.active:
            self.x -= self.speed
            self.rect.x = int(self.x)
            if self.rect.right < 0:  # 移出屏幕时失效
                self.kill()
                bgm.stop()
                pygame.mixer.Sound(resource_path("src/end.mp3")).play()
                pygame.mixer.Sound(resource_path("src/end2.mp3")).play()
                global loseend
                global running
                running = False
                loseend = 1

class SYX(pygame.sprite.Sprite):  # 僵尸类
    def __init__(self, y_pos):
        super().__init__()
        self.image = pygame.image.load(resource_path("src/syx.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(1080, y_pos))  # 从右侧生成
        self.x = 1080.0  # 使用浮点数表示x位置
        self.speed = 2        # 移动速度
        self.active = True      # 存活状态
        self.hp = 50

    def update(self):  # 僵尸移动逻辑
        if self.active:
            self.speed += 1
            if self.speed > 10:
                self.speed = -5
            self.x -= self.speed
            self.rect.x = int(self.x)
            if self.rect.right < 0:  # 移出屏幕时失效
                self.kill()
                bgm.stop()
                pygame.mixer.Sound(resource_path("src/end.mp3")).play()
                pygame.mixer.Sound(resource_path("src/end2.mp3")).play()
                global loseend
                global running
                running = False
                loseend = 1

class LHY(pygame.sprite.Sprite):  # 僵尸类
    def __init__(self, y_pos):
        super().__init__()
        self.image = pygame.image.load(resource_path("src/lhy.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(1080, y_pos + 20))  # 从右侧生成
        self.x = 1080.0  # 使用浮点数表示x位置
        self.speed = 0.6        # 移动速度
        self.active = True      # 存活状态
        self.hp = 40

    def update(self):  # 僵尸移动逻辑
        if self.active:
            self.x -= self.speed
            self.rect.x = int(self.x)
            if self.rect.right < 0:  # 移出屏幕时失效
                self.kill()
                bgm.stop()
                pygame.mixer.Sound(resource_path("src/end.mp3")).play()
                pygame.mixer.Sound(resource_path("src/end2.mp3")).play()
                global loseend
                global running
                running = False
                loseend = 1

class LHY2(pygame.sprite.Sprite):  # 僵尸类
    def __init__(self, x_pos,y_pos):
        super().__init__()
        self.image = pygame.image.load(resource_path("src/lhy2.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x_pos, y_pos ))  # 从右侧生成
        self.x = float(x_pos)  # 使用浮点数表示x位置
        self.speed = 3        # 移动速度
        self.active = True      # 存活状态
        self.hp = 80

    def update(self):  # 僵尸移动逻辑
        if self.active:
            self.x -= self.speed
            self.rect.x = int(self.x)
            if self.rect.right < 0:  # 移出屏幕时失效
                self.kill()
                bgm.stop()
                pygame.mixer.Sound(resource_path("src/end.mp3")).play()
                pygame.mixer.Sound(resource_path("src/end2.mp3")).play()
                global loseend
                global running
                running = False
                loseend = 1

class ZJT(pygame.sprite.Sprite):  # 僵尸类
    def __init__(self, y_pos):
        super().__init__()
        self.image = pygame.image.load(resource_path("src/zjt.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(1080, y_pos))  # 从右侧生成
        self.x = 1080.0  # 使用浮点数表示x位置
        self.speed = 0.25        # 移动速度
        self.active = True      # 存活状态
        self.hp = 10

    def update(self):  # 僵尸移动逻辑
        if self.active:
            self.x -= self.speed
            self.rect.x = int(self.x)
            if self.rect.right < 0:  # 移出屏幕时失效
                self.kill()
                bgm.stop()
                pygame.mixer.Sound(resource_path("src/end.mp3")).play()
                pygame.mixer.Sound(resource_path("src/end2.mp3")).play()
                global loseend
                global running
                running = False
                loseend = 1

class ZJT2(pygame.sprite.Sprite):  # 僵尸类
    def __init__(self,x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(resource_path("src/zjt2.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x_pos, y_pos))  # 从右侧生成
        self.x = float(x_pos)  # 使用浮点数表示x位置
        self.speed = 1.3        # 移动速度
        self.active = True      # 存活状态
        self.hp = 300

    def update(self):  # 僵尸移动逻辑
        if self.active:
            self.x -= self.speed
            self.rect.x = int(self.x)
            if self.rect.right < 0:  # 移出屏幕时失效
                self.kill()
                bgm.stop()
                pygame.mixer.Sound(resource_path("src/end.mp3")).play()
                pygame.mixer.Sound(resource_path("src/end2.mp3")).play()
                global loseend
                global running
                running = False
                loseend = 1
                
class FO(pygame.sprite.Sprite):  # 僵尸类
    def __init__(self, y_pos):
        super().__init__()
        self.image = pygame.image.load(resource_path("src/fo.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(1080, y_pos+20))  # 从右侧生成
        self.x = 1080.0  # 使用浮点数表示x位置
        self.speed = 0.15        # 移动速度
        self.active = True      # 存活状态
        self.hp = 200

    def update(self):  # 僵尸移动逻辑
        if self.active:
            self.x -= self.speed
            self.rect.x = int(self.x)
            if self.rect.right < 0:  # 移出屏幕时失效
                self.kill()
                bgm.stop()
                pygame.mixer.Sound(resource_path("src/end.mp3")).play()
                pygame.mixer.Sound(resource_path("src/end2.mp3")).play()
                global loseend
                global running
                running = False
                loseend = 1

class SYX2(pygame.sprite.Sprite):  # 僵尸类
    def __init__(self, y_pos):
        super().__init__()
        self.image = pygame.image.load(resource_path("src/syx2.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(1080, y_pos + 20))  # 从右侧生成
        self.x = 1080.0  # 使用浮点数表示x位置
        self.y= float(y_pos + 20)
        self.speed = 1.5        # 移动速度
        self.speed_y = 1
        self.active = True      # 存活状态
        self.hp = 50

    def update(self):  # 僵尸移动逻辑
        if self.active:
            self.x -= self.speed
            self.y += self.speed_y
            if self.y > 600:
                self.speed_y = -1
            if self.y < 100:
                self.speed_y = 1
            self.rect.x = int(self.x)
            self.rect.y = int(self.y)
            if self.rect.right < 0:  # 移出屏幕时失效
                self.kill()
                bgm.stop()
                pygame.mixer.Sound(resource_path("src/end.mp3")).play()
                pygame.mixer.Sound(resource_path("src/end2.mp3")).play()
                global loseend
                global running
                running = False
                loseend = 1

class CYY(pygame.sprite.Sprite):  # 僵尸类
    def __init__(self, y_pos):
        super().__init__()
        self.image = pygame.image.load(resource_path("src/cyy.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(1080, y_pos + 20))  # 从右侧生成
        self.x = 1080.0  # 使用浮点数表示x位置
        self.speed = 15        # 移动速度
        self.active = True      # 存活状态
        self.hp = 80

    def update(self):  # 僵尸移动逻辑
        if self.active:
            self.speed-=0.1
            if self.speed<=10:
                self.speed=0.2
            self.x -= self.speed
            self.rect.x = int(self.x)
            if self.rect.right < 0:  # 移出屏幕时失效
                self.kill()
                bgm.stop()
                pygame.mixer.Sound(resource_path("src/end.mp3")).play()
                pygame.mixer.Sound(resource_path("src/end2.mp3")).play()
                global loseend
                global running
                running = False
                loseend = 1
       
class MeiJi(pygame.sprite.Sprite):  # 未知功能类（疑似植物）
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(resource_path("src/meiji.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y + 100))
        self.speed = 4

    def update(self):  # 移动和生成检测
        self.rect.x += self.speed
        if self.rect.x > 1080:  # 到达指定位置后标记
            self.kill()
    
class LJC(pygame.sprite.Sprite):  # 未知功能类（疑似植物）
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(resource_path("src/ljc2.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y + 100))
        self.speed = 5

    def update(self):  # 移动和生成检测
        self.rect.x += self.speed
        if self.rect.x > 1080:  # 到达指定位置后标记
            self.kill()       
            
def main():  # 主游戏逻辑
    # 显示初始化
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('ruarua vs zombies')  # 窗口标题
    clock = pygame.time.Clock()  # 帧率控制器
    pygame.display.set_icon(pygame.image.load(resource_path("src/rua.png")))

    # 资源加载
    font = pygame.font.SysFont('dengxian', 20)  # 中文字体
    grass = pygame.image.load(resource_path("src/grass.png")).convert()  # 背景贴图
    smallrua = pygame.image.load(resource_path("src/smallrua.png")).convert_alpha()
    cost_text = font.render('350阳光按空格全屏弹幕       400阳光按F发射液压机     100阳光按e增加攻速     英文键盘wasd移动', True, (255,220,0))  # 装饰性文字
    yeya1_sound = pygame.mixer.Sound(resource_path("src/yeya1.mp3"))
    yeya2_sound = pygame.mixer.Sound(resource_path("src/yeya2.mp3"))
    bgm.play(-1)  # -1 表示循环播放 music.mp3
    pygame.mixer.Sound(resource_path("src/start.mp3")).play()   # 播放 start.mp3 一次
    # 游戏对象初始化
    sun_counter = SunCounter()
    player = Player()
    all_sprites = pygame.sprite.Group(player)  # 精灵容器
    zombies = pygame.sprite.Group()
    meijis = pygame.sprite.Group()
    boss_group = pygame.sprite.Group()
    ljcs=pygame.sprite.Group()
    
    z_speed = 2000
    times=0
    end=0
    rush=0
    meiji_speed=1001
    # 僵尸生成定时器（每2000ms触发）
    ZOMBIE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ZOMBIE_EVENT, z_speed)
    MEIJI_EVENT = pygame.USEREVENT + 2
    pygame.time.set_timer(MEIJI_EVENT, meiji_speed)
    SPEED_UP_EVENT = pygame.USEREVENT + 3
    pygame.time.set_timer(SPEED_UP_EVENT, 2001)
    LAST_ATTACK_EVENT = pygame.USEREVENT + 4
    pygame.time.set_timer(LAST_ATTACK_EVENT, 1000000)
    BIG_EVENT = pygame.USEREVENT + 5
    BOSS_EVENT = pygame.USEREVENT + 6
    BOSSRUSH_EVENT = pygame.USEREVENT + 7
    pygame.time.set_timer(BOSS_EVENT, 8000)
    LJC_EVENT = pygame.USEREVENT + 8
    # 在设置视频模式之后加载 loserua 图像
    global loseend
    global winend
    global running
    loserua = pygame.image.load(resource_path("src/loserua.png")).convert_alpha()
    loserua_rect = loserua.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    winrua = pygame.image.load(resource_path("src/winrua2.png")).convert_alpha()
    winrua_rect = winrua.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    bosss=list(range(0,9))
    random.shuffle(bosss)
    
    while running:
        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:  # WASD控制
                if event.key == pygame.K_w:
                    player.move_y(-130)
                elif event.key == pygame.K_s:
                    player.move_y(130)
                elif event.key == pygame.K_a:
                    player.move_x(-95)
                elif event.key == pygame.K_d:
                    player.move_x(95)
                elif event.key == pygame.K_e and sun_counter.sun >= 100 and meiji_speed > 202:
                    sun_counter.sun -= 100
                    meiji_speed -= 50
                    pygame.time.set_timer(MEIJI_EVENT, meiji_speed)
                elif event.key == pygame.K_SPACE and sun_counter.sun >= 350:
                    sun_counter.sun -= 350
                    pygame.time.set_timer(BIG_EVENT, 120)
                    pygame.mixer.Sound(resource_path("src/big.mp3")).play()
                elif event.key == pygame.K_f and sun_counter.sun >= 400:
                    sun_counter.sun -= 400
                    ya=random.choice([0,1])
                    if ya == 0:
                        yeya1_sound.play()
                    else:
                        yeya2_sound.play()
                    pygame.event.post(pygame.event.Event(LJC_EVENT))
            if event.type == ZOMBIE_EVENT:  # 生成僵尸
                y_pos = random.choice([60,180, 300, 410,560])
                zombies.add(Zombie(y_pos))
                
            if event.type == MEIJI_EVENT:  # 生成meiji
                y=player.rect.y
                x=player.rect.x
                meijis.add(MeiJi(x,y))
                
            if event.type == SPEED_UP_EVENT:  # 更新z_speed
                if z_speed > 100:
                    z_speed -= 50
                    pygame.time.set_timer(ZOMBIE_EVENT, z_speed)
                    if z_speed == 100:
                        pygame.mixer.Sound(resource_path("src/final.mp3")).play()
                        pygame.time.set_timer(BOSSRUSH_EVENT, 4000)
                        pygame.time.set_timer(LAST_ATTACK_EVENT, 8000)
                        pygame.time.set_timer(SPEED_UP_EVENT, 1000000)
                        
            if event.type == LAST_ATTACK_EVENT:
                pygame.time.set_timer(ZOMBIE_EVENT, 1000000)
                end=1
            
            if event.type == BOSSRUSH_EVENT:
                rush=1
                for i in range(0,3):
                    add = random.choice(range(0, 9))
                    bosss.append(add)
                pygame.time.set_timer(BOSS_EVENT, 100)
                pygame.time.set_timer(BOSSRUSH_EVENT, 0)
                end=1
                    
            if len(zombies) == 0 and len(boss_group)==0 and end==1:
                bgm.stop()
                pygame.mixer.Sound(resource_path("src/win.mp3")).play()
                running = 0
                winend=1
                
            if event.type == BIG_EVENT:
                times+=1
                meijis.add(MeiJi(-10,-10))
                meijis.add(MeiJi(-10,120))
                meijis.add(MeiJi(-10,250))
                meijis.add(MeiJi(-10,380))
                meijis.add(MeiJi(-10,510))
                if times==3:
                    pygame.time.set_timer(BIG_EVENT, 1000000)
                    times=0
                    
            if event.type == BOSS_EVENT:
                if not bosss:  # 检查 boss 列表是否为空
                    pygame.time.set_timer(BOSS_EVENT, 0)  # 停止 BOSS_EVENT 定时器
                    continue
                who=bosss.pop()
                if rush==0:
                    bosss.insert(0,who)
                y = random.choice([70, 180, 320, 430, 580])
                match who:
                    case 0:
                        boss_group.add(YJH(y))
                    case 1:
                        boss_group.add(ZZS(y))
                    case 2:
                        boss_group.add(XGF(y))
                    case 3:
                        boss_group.add(SYX(y))
                    case 4:
                        boss_group.add(FO(y))
                    case 5:
                        boss_group.add(LHY(y))
                    case 6:
                        boss_group.add(ZJT(y))
                    case 7:
                        boss_group.add(SYX2(y))
                    case 8:
                        boss_group.add(CYY(y))
            if event.type == LJC_EVENT:
                y=player.rect.y
                x=player.rect.x
                ljcs.add(LJC(x,y))
                
        for meiji in meijis.copy():  
            for zombie in zombies.copy():
                if pygame.sprite.collide_rect(zombie, meiji):
                    meiji.kill()
                    zombie.kill()
                    sun_counter.sun += 5
                    pygame.mixer.Sound(resource_path("src/hit.mp3")).play()
        
        for ljc in ljcs.copy():  
            for zombie in zombies.copy():
                if pygame.sprite.collide_rect(zombie, ljc):
                    overlap_rect = ljc.rect.clip(zombie.rect)
                    overlap_area = overlap_rect.width * overlap_rect.height
                    ljc_area = ljc.rect.width * ljc.rect.height
                    zombie_area = zombie.rect.width * zombie.rect.height
                    total_area = ljc_area + zombie_area - overlap_area
                    overlap_ratio = overlap_area / total_area
                    if overlap_ratio > 0.2:
                        zombie.kill()
                        sun_counter.sun += 5
                        pygame.mixer.Sound(resource_path("src/bian.mp3")).play()
            for boss in boss_group.copy():
                if pygame.sprite.collide_rect(boss, ljc):
                    overlap_rect = ljc.rect.clip(boss.rect)
                    overlap_area = overlap_rect.width * overlap_rect.height
                    ljc_area = ljc.rect.width * ljc.rect.height
                    boss_area = boss.rect.width * boss.rect.height
                    total_area = ljc_area + boss_area - overlap_area
                    overlap_ratio = overlap_area / total_area
                    if overlap_ratio > 0.2:
                        if isinstance(boss,ZJT):
                            boss_group.add(ZJT2(boss.rect.x,boss.rect.y))
                            boss.kill()
                        elif isinstance(boss,ZJT2):
                            pygame.mixer.Sound(resource_path("src/big.mp3")).play()
                            pygame.mixer.Sound(resource_path("src/zjtsong.mp3")).play()
                        else:
                            boss.hp -= 200
                            if boss.hp <= 0:
                                boss.kill()
                                sun_counter.sun += 20
                        pygame.mixer.Sound(resource_path("src/bian.mp3")).play()
                    
        for meiji in meijis.copy():  
            for boss in boss_group.copy():
                if pygame.sprite.collide_rect(boss, meiji):
                    meiji.kill()
                    boss.hp -= 10
                    if boss.hp <= 0:
                        if isinstance(boss,LHY):
                            boss_group.add(LHY2(boss.rect.x,boss.rect.y))
                            boss.kill()
                        else:
                            boss.kill()
                            sun_counter.sun += 50
                    pygame.mixer.Sound(resource_path("src/hit.mp3")).play()
                    
        for zombie in zombies.copy():
            if pygame.sprite.collide_rect(player, zombie):
                overlap_rect = player.rect.clip(zombie.rect)
                overlap_area = overlap_rect.width * overlap_rect.height
                player_area = player.rect.width * player.rect.height
                zombie_area = zombie.rect.width * zombie.rect.height
                total_area = player_area + zombie_area - overlap_area
                overlap_ratio = overlap_area / total_area
                if overlap_ratio > 0.3:
                    bgm.stop()
                    pygame.mixer.Sound(resource_path("src/end.mp3")).play()
                    pygame.mixer.Sound(resource_path("src/end2.mp3")).play()
                    running = False
                    loseend=1

        for boss in boss_group.copy():
            if pygame.sprite.collide_rect(player, boss):
                overlap_rect = player.rect.clip(boss.rect)
                overlap_area = overlap_rect.width * overlap_rect.height
                player_area = player.rect.width * player.rect.height
                boss_area = boss.rect.width * boss.rect.height
                total_area = player_area + boss_area - overlap_area
                overlap_ratio = overlap_area / total_area
                if overlap_ratio > 0.15:
                    bgm.stop()
                    pygame.mixer.Sound(resource_path("src/end.mp3")).play()
                    pygame.mixer.Sound(resource_path("src/end2.mp3")).play()
                    running = False
                    loseend=1
                    
        # 状态更新
        sun_counter.update()
        zombies.update()
        meijis.update()
        boss_group.update()
        ljcs.update()

        # 画面渲染
        screen.blit(grass, (0, 0))        # 绘制背景
        screen.blit(smallrua, (100, -15)) # 装饰元素
        
        # UI文字
        sun_text = font.render(f'阳光: {sun_counter.sun}', True, (255,255,0))
        screen.blit(sun_text, (28, 77))
        screen.blit(cost_text, (130, 77))

        # 绘制所有精灵
        all_sprites.draw(screen)
        zombies.draw(screen)
        meijis.draw(screen)
        boss_group.draw(screen)
        ljcs.draw(screen)

        pygame.display.flip()  # 刷新画面
        clock.tick(FPS)        # 维持帧率

    # 游戏结束后的处理
    loserua_scale_factor = 1.0
    
    while loseend==1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        loserua_scaled = pygame.transform.scale(loserua, (int(loserua_rect.width * loserua_scale_factor), int(loserua_rect.height * loserua_scale_factor)))
        loserua_scaled_rect = loserua_scaled.get_rect(center=loserua_rect.center)

        # 渲染背景和 loserua 图片
        screen.blit(grass, (0, 0))
        screen.blit(loserua_scaled, loserua_scaled_rect)

        # 更新屏幕
        pygame.display.flip()
        clock.tick(FPS)

        # 增加放大倍数
        loserua_scale_factor += 0.05
        if loserua_scale_factor > 2:
            loserua_scale_factor = 2

        # 等待一段时间后退出
        if loserua_scale_factor == 2:
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()
            
    winrua_scale_factor = 1.0
    while winend==1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        winrua_scaled = pygame.transform.scale(winrua, (int(winrua_rect.width * winrua_scale_factor), int(winrua_rect.height * winrua_scale_factor)))
        winrua_scaled_rect = winrua_scaled.get_rect(center=winrua_rect.center)

        # 渲染背景和 loserua 图片
        screen.blit(grass, (0, 0))
        screen.blit(winrua_scaled, winrua_scaled_rect)

        # 更新屏幕
        pygame.display.flip()
        clock.tick(FPS)

        # 增加放大倍数
        winrua_scale_factor += 0.05
        if winrua_scale_factor > 2.5:
            winrua_scale_factor = 2.5

        # 等待一段时间后退出
        if winrua_scale_factor == 2.5:
            pygame.time.wait(4000)
            pygame.quit()
            sys.exit()
if __name__ == "__main__":  # 程序入口
    main()