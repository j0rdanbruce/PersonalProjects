import pygame
import sys

from time import sleep

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien


class SidewaysShooter:

    def __init__(self):
        """initializes the main game, and creates game resources"""        
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Sideways Shooter')

        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
    
    def run_game(self):
        """main loop for the game"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self._update_ship()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
    
    def _check_events(self):
        """for each loop of the game it checks for player actions aka events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """sets moving flag based on player keydown event"""
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        #bullet firing    
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """sets moving flag based on player keyup event"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _update_ship(self):
        self.ship.update()

    def _fire_bullet(self):
        """creates new bullet and stores it in bullets list"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    
    def _update_bullets(self):
        """keeps track of position of bullets and number of bullets on screen"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
        
        if not self.aliens:
            self._create_fleet()
        
        self._update_alien_bullet_collisions()
    
    def _update_alien_bullet_collisions(self):
        """keeps track of aliens being shot down"""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        for alien_down in collisions:
            self._score_count_raise()
            print(f"Score: {self.stats.score_count}")

    def _score_count_raise(self):
        """adds to score if alien is shot down"""
        self.stats.score_count += 1
        

    def _update_aliens(self):
        """checks if aliens hit edge and updates position of fleet"""
        self.aliens.update()
        self._check_fleet_edges()
        self._check_aliens_bottom()
        
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print('Ship Hit!!!')
            self._ship_hit()
    

    def _create_fleet(self):
        """create a fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_y = self.settings.screen_height - (2 * alien_height)
        available_space_x = self.settings.screen_width - (2 * self.ship.rect.width) - (10 * alien_width)
        number_aliens_y = available_space_y // (2 * alien_height)
        number_rows = available_space_x // (2 * alien_width)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """creates single instance of an alien and sets its starting position"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.y = alien_height + 2 * alien_height * alien_number
        alien.rect.y = alien.y
        alien.x = self.screen.get_rect().width - 2 * alien_width * row_number
        alien.rect.x = alien.x
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        """checks if any aliens hit edge of screen and responds accordingly"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """drop the fleet and change directions"""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _check_aliens_bottom(self):
        """checks if an alien reaches the bottom and acts accordingly"""
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                print("Alien has breached the base." 
                "\nYour comrades are now dead."
                "\nRestart."
                )
                self._ship_hit()
                break
    
    def _ship_hit(self):
        """if ship is hit or alien reaches bottom, 
        the fleet is reset, the ship is reset to starting position, 
        and ship life goes down"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            self.aliens.empty()
            self.bullets.empty()

            self.ship.recenter_ship()
            self._create_fleet()

            self.ship_hit_counter()
            sleep(0.5)
            
        else:
            self.stats.game_active = False

    def ship_hit_counter(self):
        """keeps track of how many times ship is hit and how many lives have left"""
        self.stats.hit_counter += 1
        print(f"Your ship has been hit {self.stats.hit_counter} time(s)."
        f"\nYou have {self.stats.ships_left} lives left.")


    def _update_screen(self):
        """updates screen for each loop of game being run"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()
    

if __name__ == '__main__':
    ss = SidewaysShooter()
    ss.run_game()




