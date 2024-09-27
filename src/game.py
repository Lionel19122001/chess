import pygame

from const import *
from board import Board
from square import Square
from dragger import Dragger


class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
   
    # blit Methods
    def show_bg(self, surface):
         # Vẽ chữ trên viền
        letters = 'ABCDEFGH'  # Chữ cho hàng ngang
        numbers = '12345678'  # Số cho hàng dọc
        font = pygame.font.SysFont('Arial', FONT_SIZE)
        # Draw the board 
        for row in range(ROWS):
            for col in range(COLS):
                # if (row + col) % 2 == 0:
                #     color = (255, 255, 255) # White color
                # else:
                #     color = (0, 0, 0) # Black color
                    
                # rect = (col * SQUARE_SIZE , row * SQUARE_SIZE , SQUARE_SIZE, SQUARE_SIZE)
                
                # pygame.draw.rect(surface, color, rect)
                
                # pygame.draw.rect(surface, BROWN, pygame.Rect(-10, -10, 600, 600), 20)
                # pygame.draw.rect(surface, BLUE, pygame.Rect(600, 0, 200, HEIGHT), 5)
                x = col * SQUARE_SIZE + FRAME_WIDTH
                y = row * SQUARE_SIZE + FRAME_WIDTH
                color = (234,235,200) if (row + col) % 2 == 0 else (119,154,88)
                pygame.draw.rect(surface, color, pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE))
        
        for row in range(ROWS):
            letter_text = font.render(letters[row], True, BROWN)
            surface.blit(letter_text, (row * SQUARE_SIZE + FRAME_WIDTH + SQUARE_SIZE // 2 - FONT_SIZE // 2, 30))  # Trên
            surface.blit(letter_text, (row * SQUARE_SIZE + FRAME_WIDTH + SQUARE_SIZE // 2 - FONT_SIZE // 2, HEIGHT + FRAME_WIDTH + 10))
            
        for col in range(COLS):
            number_text = font.render(numbers[col], True, BROWN)
            surface.blit(number_text, (30, col * SQUARE_SIZE + FRAME_WIDTH + SQUARE_SIZE // 2 - FONT_SIZE // 2))  # Trái
            surface.blit(number_text, (WIDTH + FRAME_WIDTH + 10, col * SQUARE_SIZE + FRAME_WIDTH + SQUARE_SIZE // 2 - FONT_SIZE // 2))  # Phải
        
    
    
    
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    
                    img = pygame.image.load(piece.texture)
                    img_center = col * SQUARE_SIZE + FRAME_WIDTH + SQUARE_SIZE // 2 ,row * SQUARE_SIZE + FRAME_WIDTH + SQUARE_SIZE // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)
                    

                   
       
                
                
                






