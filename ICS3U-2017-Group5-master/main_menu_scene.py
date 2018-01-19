# Created by: Malcolm McCarthy
# Created in Jan 2018
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
import ui

from game_scene import *
from help_scene import *
from about_scene import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene

        self.backcolor = SpriteNode(color = (1.0, 1.0, 1.0),
                                     parent = self,
                                     position = self.size/2,
                                     size = self.size)
                                     
        self.bg = Vector2()   
        self.bg.x = self.size.x / 2
        self.bg.y = self.size.y / 2
        self.background = SpriteNode('./assets/sprites/stadium_background.png',
                                     position = self.bg,
                                     parent = self,
                                     size = self.size)                         
        start_button_position = self.size/2
        start_button_position.y = start_button_position.y + 100
        self.start_button = SpriteNode('./assets/sprites/start_button.png',
                                       parent = self,
                                       position = start_button_position)
       
        help_button_position = self.size/2
        help_button_position.y = help_button_position.y - 100
        self.help_button = SpriteNode('./assets/sprites/help_button.png',
                                       parent = self,
                                       position = help_button_position)
        
        about_button_position = self.size/2
        about_button_position.y = about_button_position.y - 300
        self.about_button = SpriteNode('./assets/sprites/about_button.png',
                                       parent = self,
                                       position = about_button_position)
        title_position = Vector2()
        title_position.x = title_position.x + 500
        title_position.y = title_position.y + 600
        self.title= LabelNode(text = 'FOOTBALLER',
                                  font = ('Copperplate', 80),
                                  parent = self,
                                  position = title_position )
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        # if the start button is pressed, the game scene will pop up
        if self.start_button.frame.contains_point(touch.location):
            
            self.present_modal_scene(GameScene())
            
        # if help button is pressed, the help scene will pop up
        if self.help_button.frame.contains_point(touch.location):
            
            self.present_modal_scene(HelpScene())
        # if the about button is pressed, about scene will pop up
        if self.about_button.frame.contains_point(touch.location):
            
            self.present_modal_scene(AboutScene())
    
    
