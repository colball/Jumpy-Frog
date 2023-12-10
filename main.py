import pygame, simpleGE, random
pygame.init()


class Frog(simpleGE.SuperSprite): 
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("frog.png")
        self.setSize(50, 50)
        self.setPosition((100,100))
    
    def checkEvents(self):
        self.addForce(.1, 270)
        if self.scene.isKeyPressed(pygame.K_SPACE):
            self.setDY(0)
            self.addForce(5, 90)
            self.jumpSound = simpleGE.Sound('Jump.wav')

class Barrier(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.imageMaster = pygame.Surface((80, 200))
        self.imageMaster.fill(pygame.Color('green'))
        self.setPosition((600,0))
        self.setDX(-3)
        
    
    def checkBounds(self):
        
        if self.x < 0:
            self.scene.reset()
        
        
    def checkEvents(self):
        if self.collidesWith(self.scene.frog):
            self.scene.reset()
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.frog = Frog(self)
        self.upperBarrier = Barrier(self)
        self.lowerBarrier = Barrier(self)
        self.background=pygame.image.load("forest.jpg")
        self.background = pygame.transform.scale(self.background, (640,480))
        self.gap = 400
        self.reset()
        self.sprites = [self.frog, self.upperBarrier, self.lowerBarrier]
  
    def reset(self):
        self.topPosition = random.randint(0,200)
        self.bottomPosition = self.topPosition + self.gap
        self.upperBarrier.setPosition((640, self.topPosition))
        self.lowerBarrier.setPosition((640, self.bottomPosition))
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
