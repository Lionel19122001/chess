
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
        dragger =self.game.dragger
        board = self.game.board 
         
        
        
        while True:
            game.show_bg(screen)
            game.show_pieces(screen)

          
            
            
            for event in pygame.event.get():
                
                
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    
                
                    clicked_row = dragger.mouseY // SQUARE_SIZE 
                    clicked_col = dragger.mouseX// SQUARE_SIZE 

                    #print(dragger.mouseY, clicked_row)
                    # print(dragger.mouseX, clicked_col)

                    # if clicked square has a piece ?
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                #mouse motion
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        dragger.update_blit(screen)
                
                
                #click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()
                
                #exit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    



            pygame.display.update()
    

main = Main()
main.mainloop()


