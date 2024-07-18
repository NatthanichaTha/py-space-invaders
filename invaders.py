from constant import *
from utils import draw_rect_outline
from random import choice

class Alien:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, screen):
        color = NEONPINK
        draw_rect_outline(screen, color, self.x, self.y, self.width, self.height)

class Invaders:
    def __init__(self):
        #create wall of aliens
        self.invaders_per_line = 8
        rows = 8
        self.row_width = (SCREEN_WIDTH / 20) * 8
        self.block_width = 30
        self.block_height = 30
        self.space_between = 10
        self.row_x = 0
        self.row_y = 0
        self.row_width = ((self.block_width + self.space_between)*self.invaders_per_line) + self.space_between
        self.move_direction = 1

        self.alien_list = []
        x = 0
        y = 0

        for i in range(rows):
            for j in range(self.invaders_per_line+1):
                alien = Alien(x, y, self.block_width, self.block_height)
                self.alien_list.append(alien)
                x += self.block_width + self.space_between
            x = 0
            y += self.block_height + self.space_between
    
    def detect_screen_edge(self):
        print(self.row_x, self.row_width, SCREEN_WIDTH)
        if self.row_x + self.row_width >= SCREEN_WIDTH -2 or (self.move_direction == -1 and self.row_x <= 2):
            return True
        return False

    def shift(self):
        for alien in self.alien_list:
            alien.x += self.move_direction*2
        self.row_x += self.move_direction*2
    
    def lower_down(self):
        for alien in self.alien_list:
            alien.y += alien.height
    
    def move(self):
        self.shift()
        if self.detect_screen_edge():
            self.lower_down()
            self.move_direction = -self.move_direction

    def add_row(self):
        #change the y position of all the existed blocks (y+=self.block_height)
        for block in self.alien_list:
            block.y += self.block_height

        #add new row of wall by insert blocks*(self.blocks_per_line) at the first row
        x = 0 + block.x
        y = 0
        for i in range(self.invaders_per_line):
            alien = Alien(x, y, self.block_width, self.block_height)
            self.alien_list.insert(i, block)
            x += self.block_width        
        
    def draw(self, screen):
        for alien in self.alien_list:
            alien.draw(screen)