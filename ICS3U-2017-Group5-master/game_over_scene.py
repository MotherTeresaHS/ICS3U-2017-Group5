from scene import *
#from game_scene import *
class GameOverScene(Scene):
    def setup(self):
         self.game_over_position = Vector2()
         
         self.background = SpriteNode(color = 'black',
                                      parent = self,
                                      position = self.size/2,
                                      size = self.size)
         self.game_over_position.x = 500
         self.game_over_position.y = 500
         self.game_over_text = LabelNode(text = 'GAME OVER!',
                                         font=('Copperplate', 80),
                                         parent = self,
                                         position = self.game_over_position)
                                         
         self.main_menu_position = Vector2()
         self.main_menu_position.x = 450
         self.main_menu_position.y = 350
        
         self.main_menu_button = SpriteNode('./assets/sprites/main_menu.PNG',
                                            parent = self,
                                            position = self.main_menu_position,
                                            size = self.size * 2)
         
