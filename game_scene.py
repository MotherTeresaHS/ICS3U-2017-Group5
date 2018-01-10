'''
created by Malcolm McCarthy
created in January 2018
created for ICS3U
this scene shows the main game
'''

from scene import *
import ui

from main_menu_scene import *
from numpy import random
from copy import deepcopy

class GameScene(Scene):
    def setup(self):
        
        self.center_of_screen = self.size/2
        self.left_button_down = False
        self.right_button_down = False
        self.charcter_movement_speed = 22.5
        self.screen_size = deepcopy(self.size)
        self.football_geneartion_speed = 1
        self.football_drop_speed = 17
        self. footballs = []
        
        # adds the background texture
        self.bg = Vector2()   
        self.bg.x = self.size.x / 2
        self.bg.y = self.size.y / 2
        self.background = SpriteNode('./assets/sprites/football_field.JPG',
                                     position = self.bg,
                                     parent = self,
                                     size = self.size,
                                     scale = 1.15)
        
        # adds the character icon
        self.character_position = self.center_of_screen
        self.character_position.y = 100
        self.character = SpriteNode('./assets/sprites/football_character.png',
                                     parent = self,
                                     position = self.character_position,
                                     size = self.size / 3)
        
        # adds in the move left button
        move_left_button_position = self.center_of_screen
        move_left_button_position.x = 100
        self.move_left_button = SpriteNode('./assets/sprites/move_left_button.png',
                                            parent = self,
                                            position = move_left_button_position,
                                            size = self.size / 6,
                                            alpha = 0.75)
                                     
        #adds the move right button
        move_right_button_position = self.center_of_screen
        move_right_button_position.x = 900
        self.move_right_button = SpriteNode('./assets/sprites/move_right_button.png',
                                             parent = self,
                                             position = move_right_button_position,
                                             size = self.size / 6,
                                             alpha = 0.75)
        
        #adds the pause button
        pause_button_position = self.center_of_screen
        pause_button_position.x = 100
        pause_button_position.y = 675
        self.pause = SpriteNode('./assets/sprites/pause_button.png',
                                 parent = self,
                                 position = pause_button_position,
                                 size = self.size / 8,
                                 alpha = 0.5) 
        
        self.fb = Vector2()
        self.fb.x = self.size.x / 2
        self.fb.y = self.size.y -100
        self.futbol = SpriteNode('./assets/sprites/football.png', position = self.fb, parent = self, size = self.size / 4)
        
    def update(self):
        
        # moves the pair of hands when a move button is pressed
        if self.left_button_down == True:
            self.character.run_action(Action.move_by(-1*self.charcter_movement_speed, 0.0, 0.1))
        
        if self.right_button_down == True:
            self.character.run_action(Action.move_by(self.charcter_movement_speed, 0.0, 0.1))
        #self.futbol.run_action(Action.move_to(self.size.x / 2, character_position.y, 2.5))
            
         time 
    def touch_began(self, touch):
        # function is called every time a button is pressed
        
        # check if left or right button is down
        if self.move_left_button.frame.contains_point(touch.location):
            self.left_button_down = True
            self.generate_new_football()
            
        if self.move_right_button.frame.contains_point(touch.location):
            self.right_button_down = True
        self.generate_new_football()
        
    def touch_ended(self, touch):
        # this function is called everytime the user removes their finger from the screen
        # the character icon will stop moving
        self.left_button_down = False
        self.right_button_down = False
        
        '''
    def football(self):
    	self.fb = Vector2()
    	self.fb.x = self.size.x / 2
    	self.fb.y = self.size.y / 2
    	self.futbol = SpriteNode('./assets/sprites/football.png', position = self.fb, parent = self, size = self.size / 8)
    '''
    def generate_new_football(self):
        # generates a new football to come down the screen
        
        football_starting_position = deepcopy(self.screen_size) 
        football_starting_position.x = random.randint(100, self.screen_size.x - 100)
        football_starting_position.y = football_starting_position.y + 200
        
        football_ending_location = deepcopy(self.screen_size)
        football_ending_location.x = random.randint(100, self.screen_size.x - 100)
        football_ending_location.y = 100
        
        self.footballs.append(SpriteNode('./assets/sprites/football.png',
                                         position = football_starting_position,
                                         parent = self, size = self.size / 8))
        
        footballMoveAction = Action.move_to(football_ending_location.x, 
                                         football_ending_location.y, 
                                         self.football_drop_speed,
                                         TIMING_SINODIAL)
        self.footballs[len(self.footballs)-1].run_action(footballMoveAction)
