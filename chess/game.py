import pygame
from .constants import WHITE,BLACK, BLUE, SQUARE_SIZE
from .board import Board
from .piece import King

class Game:
    def __init__(self, win):
        self.win = win
        self.board = Board(win)
        self.turn = WHITE
        self.valid_moves = {}
        self.valid_bl_king = {}
        self.valid_wh_king = {}
        self.bl_check = False
        self.wh_check = False #white is in Check
        self.selected = None #Is a piece selected?

    def update(self):
        self.board._draw()
        self.draw_valid_moves()
        pygame.display.update()

    def draw_valid_moves(self):
       for move in self.valid_moves:
           row,col = move
           pygame.draw.circle(self.win, BLUE, (col*SQUARE_SIZE + SQUARE_SIZE//2, row *SQUARE_SIZE+ SQUARE_SIZE//2), 15) 
    
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    def select(self, row, col):
        #this is where we interact with the main, because we only have access to game. So, under the hood I need to get the piece this 
        #corresponds to and then return the valid moves to self.valid_moves. Maybe I can get a piece from the board and then that piece
        #can use its get_valid_moves and return them
        if self.selected:
            result = self._move(row,col) 
            '''if check:
                if piece.color == WHITE:
                    self.bl_check = False
                else:
                    self.wh_check = True ''' #need to have a way to determine check. Maybe after a piece moves, check its valid moves
                                             #against the opposing player's king's valid moves. If they intersect, remove those moves from
                                             #the king's moves. And if it puts the king in check, create an alert and only allow moves
                                             #getting out of check. Maybe a hash map of all pieces on a team. Determine all possible moves
                                             #from all possible pieces and then see if any can get the king out of check, if not that is checkmate
            if not result:
                self.selected = None
                self.select(row,col)
                #if a move is impossible, select the next location having not selected a piece
            
        #no piece is selected as of yet
        piece = self.board.get_piece(row,col)
        if piece != 0 and piece.color == self.turn: #if a piece is here and the color is for the player who is moving now
            self.selected = piece
            self.valid_moves = piece.get_valid_moves(self.board)
            
            #stores the valid moves of a king. These will be compared later with the new valid moves of piece for check 
            if isinstance(piece, King):
                if piece.color == WHITE:
                    self.valid_wh_king = self.valid_moves
                else:
                    self.valid_bl_king = self.valid_moves
                    print(self.valid_bl_king)

            return True
        return False

    def _move(self,row,col):
        piece = self.board.get_piece(row,col) 
        if self.selected and (row,col) in self.valid_moves:
            if self.valid_moves[(row,col)]:
                self.board.remove(self.valid_moves[(row,col)][0]) #index zero stores the piece to be removed.
                                                                  #in the case of a castle, the second index stores the new location of the rook
                if len(self.valid_moves[(row,col)]) > 1:
                    if self.valid_moves[(row,col)][1]:
                        self.board.create_rook(self.valid_moves[(row,col)][1])
            self.board.move(self.selected, row, col) 
            self.change_turn()
        else:
            return False
        
        return True