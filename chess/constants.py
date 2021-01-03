#images from https://opengameart.org/content/chess-pieces
import pygame

WIDTH, HEIGHT = 640,640
ROWS, COLS = 8,8
SQUARE_SIZE = WIDTH // COLS


BROWN = (64,64,64)
TAN = (255,178,102)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,255,0)

#CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (36,28))
BLPAWN = pygame.transform.scale(pygame.image.load('assets/black_pawn.png'), (50,67))
WHPAWN = pygame.transform.scale(pygame.image.load('assets/white_pawn.png'), (50,67))
BLROOK = pygame.transform.scale(pygame.image.load('assets/black_rook.png'), (50,67))
WHROOK = pygame.transform.scale(pygame.image.load('assets/white_rook.png'), (50,67))
BLKNGT = pygame.transform.scale(pygame.image.load('assets/black_knight.png'), (50,67))
WHKNGT = pygame.transform.scale(pygame.image.load('assets/white_knight.png'), (50,67))
BLBISH = pygame.transform.scale(pygame.image.load('assets/black_bishop.png'), (50,67))
WHBISH = pygame.transform.scale(pygame.image.load('assets/white_bishop.png'), (50,67))
BLQUEN = pygame.transform.scale(pygame.image.load('assets/black_queen.png'), (50,67))
WHQUEN = pygame.transform.scale(pygame.image.load('assets/white_queen.png'), (50,67))
BLKING = pygame.transform.scale(pygame.image.load('assets/black_king.png'), (50,67))
WHKING = pygame.transform.scale(pygame.image.load('assets/white_king.png'), (50,67))