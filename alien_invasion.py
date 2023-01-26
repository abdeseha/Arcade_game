import pygame

import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from fond import space
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Meke the play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    fond = space(screen)

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets and alines.
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update() 
            gf.update_bullets(ai_settings, screen, ship, stats, sb, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(screen,fond, stats, sb, ship, bullets, aliens, play_button)
              
run_game()