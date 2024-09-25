import pygame

from const import *
from board import Board
from square import Square


class Game:
    def __init__(self):
        self.board = Board()
    
    
    # Show Methods
    def show_bg(self, surface):
        
        # Draw the board 
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (255, 255, 255) # White color
                else:
                    color = (0, 0, 0) # Black color
                    
                rect = (col * SQUARE_SIZE , row * SQUARE_SIZE , SQUARE_SIZE, SQUARE_SIZE)
                
                pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(surface, BROWN, pygame.Rect(0, 0, 600, HEIGHT), 5)
                pygame.draw.rect(surface, BLUE, pygame.Rect(600, 0, 200, HEIGHT), 5)
        
        
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    
                    img = pygame.image.load(piece.texture)
                    img_center = col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)
            
                
                
                






