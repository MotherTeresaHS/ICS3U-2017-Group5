from scene import *
from game_scene import *
from main_menu_scene import *

class PauseScene(Scene):
    def setup(self):
        resume_button_position = Vector2()
        resume_button_position.x = 450
        resume_button_position.y = 700
        
        self.backcolor = SpriteNode(color = 'Black',
                                     parent = self,
                                     position = self.size / 2,
                                     size = self.size)
                                     
        
        self.resume_button = SpriteNode('./assets/sprites/resume_button.PNG',
                                   parent = self,
                                   position = resume_button_position,
                                   size = self.size * 2)
        self.main_menu_position = Vector2()
        self.main_menu_position.x = 450
        self.main_menu_position.y = 350
        
        self.main_menu_button = SpriteNode('./assets/sprites/main_menu.PNG',
                                            parent = self,
                                            position = self.main_menu_position,
                                            size = self.size * 2)
        
    
    def touch_began(self, touch):
        if self.resume_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
            
        if self.main_menu_button.frame.contains_point(touch.location):
        	  self.dismiss_modal_scene()
        	  self.dismiss_modal_scene()
