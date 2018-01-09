'''
created by Malcolm McCarthy
created in January 2018
created for ICS3U
this scene shows the main game
'''

from scene import *
import ui

from main_menu_scene import *

class GameScene(Scene):
    def setup(self):
        
        self.center_of_screen = self.size/2
        self.left_button_down = False
        self.right_button_down = False
        self.charcter_movement_speed = 22.5
        
        # adds the background texture
        self.bg = Vector2()   
        self.bg.x = self.size.x / 2
        self.bg.y = self.size.y / 2
        self.background = SpriteNode('./assets/sprites/football_field.JPG',
                                     position = self.bg,
                                     parent = self,
                                     size = self.size,
                                     scale = 1.15)
                                     
        character_position = self.center_of_screen
        character_position.y = 100
        self.character = SpriteNode('./assets/sprites/character.JPG',
                                     parent = self,
                                     position = character_position,
                                     size = self.size / 5)
        
        move_left_button_position = self.center_of_screen
        move_left_button_position.x = 100
        self.move_left_button = SpriteNode('./assets/sprites/move_left_button.png',
                                            parent = self,
                                            position = move_left_button_position,
                                            size = self.size / 6)
                                     
        move_right_button_position = self.center_of_screen
        move_right_button_position.x = 900
        self.move_right_button = SpriteNode('./assets/sprites/move_right_button.png',
                                             parent = self,
                                             position = move_right_button_position,
                                             size = self.size / 6)
        
        pause_button_position = self.center_of_screen
        pause_button_position.x = 100
        pause_button_position.y = 675
        self.pause = SpriteNode('./assets/sprites/pause_button.png',
                                 parent = self,
                                 position = pause_button_position,
                                 size = self.size / 8) 
        
    def update(self):
        
        # move spaceship if button is pressed down
        if self.left_button_down == True:
            self.character.run_action(Action.move_by(-1*self.charcter_movement_speed, 0.0, 0.1))
        if self.right_button_down == True:
            self.character.run_action(Action.move_by(self.charcter_movement_speed, 0.0, 0.1))
            
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        # check if left or right button is down
        if self.move_left_button.frame.contains_point(touch.location):
            self.left_button_down = True
        
        if self.move_right_button.frame.contains_point(touch.location):
            self.right_button_down = True
            
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if I removed my finger, then no matter what spaceship
        #    should not be moving any more
        self.left_button_down = False
        self.right_button_down = False
