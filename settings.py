class Settings():
    '''基础数据'''
    def __init__(self):
        #屏幕的宽，高，颜色
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        #飞机的飞行速度'''
        self.ship_speed_factor = 1.5
        #子弹的基础数据
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60