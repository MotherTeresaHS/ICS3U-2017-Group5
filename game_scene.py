'''
created by Malcolm McCarthy
created in January 2018
created for ICS3U
this scene shows the main game
'''

from scene import *
import ui

from game_over_scene import *
from pause_scene import * 
from main_menu_scene import *
from numpy import random
from copy import deepcopy
import sound
class GameScene(Scene):
    def setup(self):
    	
        # global variables
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.scoreboard_position = Vector2()
        self.center_of_screen = self.size/2
        self.left_button_down = False
        self.right_button_down = False
        self.character_movement_speed = 22.5
        self.screen_size = deepcopy(self.size)
        self.football_generation_speed = 1
        self.football_drop_speed = 10
        self.footballs = []
        self.score = 0
        self.counter = 1
        self.life_bar_position = Vector2()
        self.center_of_screen = self.size / 2
        self.alive = True
        
        # adds the background texture
        self.background_position = Vector2()   
        self.background_position.x = self.size.x / 2
        self.background_position.y = self.size.y / 2
        self.background = SpriteNode('./assets/sprites/football_field.PNG',
                                     position = self.background_position,
                                     parent = self,
                                     size = self.size,
                                     scale = 1.15)
        
        # adds the character icon
        self.character_position = self.center_of_screen
        self.character_position.y = 100
        self.character = SpriteNode('./assets/sprites/football_character.png',
                                     parent = self,
                                     position = self.character_position,
                                     size = self.size /4)
        
        # adds in the move left button
        move_left_button_position = self.center_of_screen
        move_left_button_position.x = 100
        self.move_left_button = SpriteNode('./assets/sprites/move_left.PNG',
                                            parent = self,
                                            position = move_left_button_position,
                                            size = self.size / 8)
                                   
        #adds the move right button
        move_right_button_position = self.center_of_screen
        move_right_button_position.x = 850
        self.move_right_button = SpriteNode('./assets/sprites/move_right.PNG',
                                             parent = self,
                                             position = move_right_button_position,
                                             size = self.size / 8)
        
        #adds the pause button
        leave_button_position = self.center_of_screen
        leave_button_position.x = 100
        leave_button_position.y = 675
        self.leave = SpriteNode('./assets/sprites/leave.PNG',
                                 parent = self,
                                 position = leave_button_position,
                                 size = self.size ) 
        
        # adds the score board in the top right corner
        self.scoreboard_position.x = 900
        self.scoreboard_position.y = self.size_of_screen_y - 50
        self.scoreboard_label = LabelNode(text = 'Score: 0',
                                     font=('Copperplate', 46),
                                     parent = self,
                                     position = self.scoreboard_position)
        
        # adds the lives bar under the score board
        self.life_bar_position.x = 900
        self.life_bar_position.y = self.size_of_screen_y - 150
        self.life_bar_label = LabelNode(text = 'Lives: 1',
                                     font=('Copperplate', 46),
                                     parent = self,
                                     position = self.life_bar_position)
    def update(self):
        # updates 60 times a second
        # moves the pair of hands when a move button is pressed
        if (self.left_button_down == True) and (self.character.position.x > 30):
            self.character.run_action(Action.move_by(-1*self.character_movement_speed, 0.0, 0.1))
        
        if (self.right_button_down == True) and (self.character.position.x < self.size.x - 30):
            self.character.run_action(Action.move_by(self.character_movement_speed, 0.0, 0.1))
            
        create_new_ball_chance = random.randint(1,101)
        if create_new_ball_chance <= self.football_generation_speed:
            self.generate_new_football()
            
        #checks if score should be updated
        if len(self.footballs) > 0 and self.character > 0:
            
            for football in self.footballs:
                if football.frame.contains_point(self.character.position):
                    #football.remove_from_parent()
                    self.footballs.remove(football)
                    football.remove_from_parent()
                    #self.footballs.remove(football)
                    self.score = self.score + 1
                    self.scoreboard_label.text = 'Score: ' + str(self.score)
                    sound.play_effect('8ve:8ve-beep-timber')
            
                    
            # tracks remaining lives
            for football in self.footballs:
                if football.position.y < 0:
                    football.remove_from_parent()
                    self.footballs.remove(football)
                    self.counter = self.counter - 1
                    self.life_bar_label.text = 'Lives: ' + str(self.counter)
                    
                    
        if self.counter == 0:
            
            sound.play_effect('8ve:8ve-slide-magic')
            self.alive = False
            #screen turns black once game is over
            self.background = SpriteNode(color = 'black',
                                      position = self.background_position,
                                      parent = self,
                                      size = self.size,
                                      scale = 1.15)
            # game over text
            self.game_over_position = Vector2()
            self.game_over_position.x = 500
            self.game_over_position.y = 500
            self.game_over_text = LabelNode(text = 'GAME OVER!',
                                         font = ('Copperplate', 80),
                                         parent = self,
                                         position = self.game_over_position)
             # button to return to main menu                        
            self.main_menu_position = Vector2()
            self.main_menu_position.x = 450
            self.main_menu_position.y = 350
            self.main_menu_button = SpriteNode('./assets/sprites/main_menu.PNG',
                                            parent = self,
                                            position = self.main_menu_position,
                                            size = self.size) 
        
        if self.character.position.x >= self.size_of_screen_x:
            self.character_position = self.size_of_screen_x - 75
        
    def touch_began(self, touch):
        # function is called every time a move button is pressed
        
        # check if left or right button is down
        if self.move_left_button.frame.contains_point(touch.location):
            self.left_button_down = True
            #self.generate_new_football()
            
        if self.move_right_button.frame.contains_point(touch.location):
            self.right_button_down = True
        #self.generate_new_football()
        
        
        
    def touch_ended(self, touch):
        # this function is called everytime the user removes their finger from the screen
        # the character icon will stop moving
        self.left_button_down = False
        self.right_button_down = False
        
        if self.leave.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
          
        
        if self.alive == False:
            if self.main_menu_button.frame.contains_point(touch.location):
                self.dismiss_modal_scene()
    
    def generate_new_football(self):
        # generates a new football to come down the screen
        
        football_starting_position = deepcopy(self.screen_size) 
        football_starting_position.x = random.randint(100, self.screen_size.x - 100)
        football_starting_position.y = football_starting_position.y + 200
        
        football_ending_location = deepcopy(self.screen_size)
        football_ending_location.x = random.randint(100, self.screen_size.x - 100)
        football_ending_location.y = - 200
        
        self.footballs.append(SpriteNode('./assets/sprites/football.png',
                                         position = football_starting_position,
                                         parent = self, size = self.size / 4))
        
        footballMoveAction = Action.move_to(football_ending_location.x, 
                                         football_ending_location.y, 
                                         self.football_drop_speed,
                                         TIMING_SINODIAL)
        self.footballs[len(self.footballs)-1].run_action(footballMoveAction)
