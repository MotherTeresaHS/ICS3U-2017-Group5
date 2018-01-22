# made by Malcolm McCarthy
# in jan 2018
#for ICS3U
#gives credit to owners of photos

from scene import *
import ui

from main_menu_scene import *

class AboutScene(Scene):
    def setup(self):
        center_of_screen = self.size/2
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'green', 
                                     parent = self, 
                                     size = self.size)
                                     
        self.about_text = LabelNode(text = 'Designed by: Malcolm McCarthy, art from www.opengameart.org',
                                      font=('Copperplate', 30),
                                      parent = self,
                                      position = self.size / 2,
                                      scale = 0.75)
        
        back_button_position = self.size
        back_button_position.x = 100
        back_button_position.y = back_button_position.y - 100
        self.back_button = SpriteNode('./assets/sprites/back.PNG',
                                       parent = self,
                                       position = back_button_position)
    def touch_began(self, touch):
        
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
