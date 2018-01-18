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
         
