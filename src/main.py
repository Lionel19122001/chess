
import pygame
import sys


from const import *
from game import Game

from square import Square




class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH + 2 * FRAME_WIDTH, HEIGHT + 2 * FRAME_WIDTH))
        pygame.display.set_caption("Chess")
        self.game = Game()
    
    
    def  mainloop(self):

        screen = self.screen
        game = self.game
         
        
        
        while True:
            game.show_bg(screen)
            game.show_pieces(screen)
            
            
            
            for event in pygame.event.get():
                
                
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game.click(event.pos[0], event.pos[1])
                
                
                #mouse motion
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                
                
                #click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
                
                #exit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    



            pygame.display.update()
    

main = Main()
main.mainloop()


