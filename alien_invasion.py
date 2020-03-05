import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    stats = GameStats(ai_settings)
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)

    while True:
        #按键操作变化
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            #图形的实际改变
            ship.update()
            #子弹图形更新及删除飞出屏幕的子弹
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, ship, bullets, aliens)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)


run_game()


