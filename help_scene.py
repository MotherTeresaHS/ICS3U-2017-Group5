import ui
from main_menu_scene import *
from scene import *

class HelpScene(Scene):
    def setup(self):
        
        center_of_screen = self.size/2
        
        self.tutorial = SpriteNode('./assets/sprites/tutorial.PNG',
        	                         position = self.size / 2, 
                                   parent = self, 
                                   size = self.size)
        back_button_position = self.size
        back_button_position.x = self.size.x - 525
        back_button_position.y = self.size.y - 50
        self.back_button = SpriteNode('./assets/sprites/back.PNG',
                                      position = back_button_position,
                                      parent = self)

    def touch_began(self, touch):
        
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
