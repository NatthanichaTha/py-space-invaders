from constant import *
from spaceship import Spaceship
from invaders import Alien, Invaders
import pygame

class Missile:
    def __init__(self, spaceship: Spaceship, invaders: Invaders):
        self.radius = 3
        self.color = WHITE
        self.spaceship = spaceship
        self.invaders = invaders 
        spaceship_center = spaceship.x + spaceship.width/2
        self.x = spaceship_center
        self.y = spaceship.y + self.radius

    def check_hit(self, alien: Alien):
        if self.y <= alien.y+alien.height and self.x >= alien.x and self.x + self.radius <= alien.x + alien.width:
            return True
        
    def handle_hit(self, alien: Alien):
        if self.check_hit(alien):
            self.invaders.alien_list.remove(alien)
            return True
        return False     
    
    def move(self):
        self.y -= 5
        for alien in self.invaders.alien_list:
            if self.handle_hit(alien):
                return True
        return False
            

    def draw(self, screen):
        pygame.draw.circle( 
        surface=screen, color=self.color, center=(self.x, self.y), radius=self.radius)
