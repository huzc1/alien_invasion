class Settings():
    '''基础数据'''
    def __init__(self):
        #屏幕的宽，高，颜色
        self.screen_width = 960
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        #飞机的飞行速度'''
        self.ship_limit = 3
        #子弹的基础数据
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int( self.alien_points * self.score_scale)