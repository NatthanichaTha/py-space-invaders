import pygame
from pygame.locals import *
from constant import *
from missile import Missile
from spaceship import Spaceship
from invaders import Alien, Invaders

class Game:
    def __init__(self):      
        # Initialise screen
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("PySpaceInvaders")

        #set timer to every 10 secends (invaders go down every 10 sec)
        self.TIMER_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.TIMER_EVENT, 10000)

        #set timer to limit shooting speed
        self.enable_shooting = pygame.USEREVENT + 2
        pygame.time.set_timer(self.enable_shooting, 333)

        # Fill background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(BG_COLOR)
        
        # Limit FPS with clock
        self.clock = pygame.time.Clock()

        # Initialise game objects (Invaders, Rocket, Fireball)
        self.invaders = Invaders()
        self.spaceship = Spaceship()
        self.missile = Missile(self.spaceship, self.invaders)
        self.missile_list = []
        self.can_shoot = True

    def game_loop(self):
        while True:
            # Events: keyboard input
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                # elif event.type == self.TIMER_EVENT:
                #     self.invaders.shift()

                elif event.type == self.enable_shooting:
                    self.can_shoot = True

            self.spaceship.move()
            self.invaders.move()
            if pygame.key.get_pressed()[pygame.K_SPACE] and self.can_shoot == True:
                missile = Missile(self.spaceship, self.invaders)
                self.missile_list.append(missile)
                self.can_shoot = False
            
            for missile in self.missile_list:
                if missile.move():
                    self.missile_list.remove(missile)


            # Rendering: first clear with background and then draw each object
            # Blit everything to the screen (make background)
            self.screen.blit(self.background, (0, 0))

            #draw ball, paddle, and blocks on the screen
            self.invaders.draw(self.screen)
            self.spaceship.draw(self.screen)
            
            for missile in self.missile_list:
                missile.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(10)