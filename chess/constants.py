#images from https://www.pikpng.com/downpngs/iRwmwRJ_chess-piece-creative-grid-horse-chess-pieces-png/
import pygame

WIDTH, HEIGHT = 640,640
ROWS, COLS = 8,8
SQUARE_SIZE = WIDTH // COLS


BROWN = (51, 33, 16)
TAN = (255,178,102)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,255,0)

BLPAWN = pygame.transform.scale(pygame.image.load('assets/new_bl_pawn.png'), (42,58))
WHPAWN = pygame.transform.scale(pygame.image.load('assets/new_wh_pawn.png'), (42,58))
BLROOK = pygame.transform.scale(pygame.image.load('assets/new_bl_rook.png'), (50,67))
WHROOK = pygame.transform.scale(pygame.image.load('assets/new_wh_rook.png'), (50,67))
BLKNGT = pygame.transform.scale(pygame.image.load('assets/new_bl_kngt.png'), (50,67))
WHKNGT = pygame.transform.scale(pygame.image.load('assets/new_wh_kngt.png'), (50,67))
BLBISH = pygame.transform.scale(pygame.image.load('assets/new_bl_bish.png'), (50,67))
WHBISH = pygame.transform.scale(pygame.image.load('assets/new_wh_bish.png'), (50,67))
BLQUEN = pygame.transform.scale(pygame.image.load('assets/new_bl_quen.png'), (50,67))
WHQUEN = pygame.transform.scale(pygame.image.load('assets/new_wh_quen.png'), (50,67))
BLKING = pygame.transform.scale(pygame.image.load('assets/new_bl_king.png'), (50,67))
WHKING = pygame.transform.scale(pygame.image.load('assets/new_wh_king.png'), (50,67))