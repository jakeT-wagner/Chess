import pygame
from .constants import *
from .piece import *

class Board:
    def __init__(self, win):
        self.board = []
        self.win = win
        self.initiate_board()
        self._draw()

    def draw_squares(self):
        self.win.fill(BROWN)
        for row in range(ROWS):
            for col in range(COLS):
                if (row+col) % 2 == 0:
                    pygame.draw.rect(self.win, TAN,(row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        
    def initiate_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)
        self.add_pieces()

    def add_pieces(self):
        for i in range(2):
            for j in range(8):
                #pawns
                if i == 1:
                    self.board[i][j] = Pawn(i,j,BLACK,BLPAWN)
                if ROWS-1-i== 6:
                    self.board[ROWS-1-i][j] = Pawn(ROWS-1-i,j,WHITE,WHPAWN)
                #rooks
                if i == 0 and (j == 0 or j == 7):
                    self.board[i][j] = Rook(i,j,BLACK,BLROOK)
                if ROWS-1-i == 7 and (j == 0 or j == 7):
                    self.board[ROWS-1-i][j] = Rook(ROWS-1-i,j, WHITE, WHROOK)
                #knights 
                if i == 0 and (j == 1 or j == 6):
                    self.board[i][j] = Knight(i,j,BLACK, BLKNGT)
                if ROWS-1-i == 7 and (j == 1 or j == 6):
                    self.board[ROWS-1-i][j] = Knight(ROWS-1-i, j, WHITE, WHKNGT)
                #bishops
                if i == 0 and (j==2 or j == 5):
                    self.board[i][j] = Bishop(i,j,BLACK,BLBISH)
                if ROWS-1-i == 7 and (j==2 or j == 5):
                    self.board[ROWS-1-i][j] = Bishop(ROWS-1-i, j, WHITE, WHBISH)
                #queens
                if i == 0 and j == 3:
                    self.board[i][j] = Queen(i,j,BLACK, BLQUEN)
                if ROWS-1-i == 7 and j ==3:
                    self.board[ROWS-1-i][j] = Queen(ROWS-1-i, j, WHITE, WHQUEN)
                #kings
                if i == 0 and j == 4:
                    self.board[i][j] = King(i,j,BLACK,BLKING)
                if ROWS-i-1 == 7 and j == 4:
                    self.board[ROWS-i-1][j] = King(ROWS-1-i, j, WHITE, WHKING)

    def create_rook(self,piece):
        self.board[piece.row][piece.col] = Rook(piece.row,piece.col, piece.color, piece.image)

    def _draw(self):
        self.draw_squares()
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    self.board[row][col].draw(self.win)
    
    def get_piece(self, row, col):
        return self.board[row][col]

    def remove(self, piece):
        self.board[piece.row][piece.col] = 0

    def move(self, piece,row,col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col] 
        #NOTICE. will have to remove the other piece before actually moving there, or it will move the destroyed piece to the 
        #destroyer's location
        piece.move(row,col) 
        piece.change_queen(self) #will only occur if it is a pawn that reaches the end of the road

    def set_grid(self, grid):
        self.board = grid

    def check_check(self, row, col, color, image):
        attackers = {}
        final_attackers = {}
        is_check = False

        attackers.update(Knight(row,col, color, image).get_valid_moves(self,row,col))
        self.remove_empty_moves(attackers, Knight)
        final_attackers.update(attackers)

        attackers.update(Bishop(row,col, color, image).get_valid_moves(self,row,col))
        self.remove_empty_moves(attackers, Bishop)
        final_attackers.update(attackers)

        attackers.update(Queen(row,col, color, image).get_valid_moves(self, row, col))
        self.remove_empty_moves(attackers, Queen)
        final_attackers.update(attackers)

        attackers.update(Rook(row,col, color, image).get_valid_moves(self, row, col))
        self.remove_empty_moves(attackers, Rook)
        final_attackers.update(attackers)

        attackers.update(Pawn(row,col, color, image).get_valid_moves(self, row, col))
        self.remove_empty_moves(attackers, Pawn)
        final_attackers.update(attackers)

        if len(final_attackers) != 0:
            is_check = True
        return is_check, attackers
        
    def remove_empty_moves(self, mydict, piece_type):
        delete = []
        for v in mydict:
            if len(mydict[v]) == 0:
                delete.append(v)
            elif not isinstance(mydict[v][0], piece_type):
                delete.append(v)
        for i in delete:
            del mydict[i]
        return mydict
    