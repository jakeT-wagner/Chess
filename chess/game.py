import pygame
from .constants import WHITE,BLACK, BLUE, SQUARE_SIZE, BLKING
from .board import Board
from .piece import King
from copy import deepcopy

class Game:
    def __init__(self, win):
        self.win = win
        self.board = Board(win)
        self.turn = WHITE
        self.valid_moves = {}
        self.wh_attackers = {}
        self.bl_attackers = {}
        self.bl_king_row = 0
        self.bl_king_col = 4
        self.wh_king_row = 7
        self.wh_king_col = 4
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
            if not result:
                self.selected = None
                self.select(row,col)
                #if a move is impossible, select the next location having not selected a piece
            
        #no piece is selected as of yet
        piece = self.board.get_piece(row,col)
        if piece != 0 and piece.color == self.turn: #if a piece is here and the color is for the player who is moving now
            self.selected = piece
            if self.turn == WHITE:
                king_row = self.wh_king_row
                king_col = self.wh_king_col
            else:
                king_row = self.bl_king_row
                king_col = self.bl_king_col
            self.valid_moves = piece.get_valid_moves(self.board, king_row, king_col)

            return True
        return False

    def _move(self,row,col):
        '''
        if self.selected.color == BLACK:
            king_row = self.bl_king_row
            king_col = self.bl_king_col
        else:
            king_row = self.wh_king_row
            king_col = self.bl_king_row
        if not self.check_valid_move(self.selected,row,col, king_row, king_col):
        '''
        if self.selected and (row,col) in self.valid_moves:
            if self.valid_moves[(row,col)]: #not an empty square
                self.board.remove(self.valid_moves[(row,col)][0]) #index zero stores the piece to be removed.
                                                                #in the case of a castle, the second index stores the new location of the rook
                if len(self.valid_moves[(row,col)]) > 1:
                        self.board.create_rook(self.valid_moves[(row,col)][1])
            self.board.move(self.selected, row, col) 

            if isinstance(self.selected, King):
                if self.selected.color == WHITE:
                    self.wh_king_row = row
                    self.wh_king_col = col
                else:
                    self.bl_king_row = row
                    self.bl_king_row = row
            #checks if either team is in check
            self.bl_check, self.bl_attackers = self.board.check_check(self.bl_king_row, self.bl_king_col, BLACK, BLKING)
            if self.bl_check == True:
                print("CHECK!, black")
            self.wh_check, self.wh_attackers = self.board.check_check(self.wh_king_row, self.wh_king_col, WHITE, BLKING)
            if self.wh_check == True:
                print("CHECK!, white")
            self.change_turn()
        else:
            return False
        
        return True
        '''
        else:
            print("this puts your king in check")
            return False
        '''
        
    
    def check_valid_move(self,piece_to_move,row,col, king_row, king_col):
        #don;t need to check for legitimacy of the move, just if by making this move, the player's king will be subject to check
        is_check = False
        temp_board = Board(self.win)
        temp_grid = deepcopy(self.board.board)
        #CANT COPY FOR SOME REASON!!!!!!!!!
        temp_board.set_grid(temp_grid)
        piece_removed = temp_board.get_piece(row,col)  
        if piece_removed != 0:
            temp_board.remove(piece_removed)
        temp_board.move(temp_board.get_piece(piece_to_move.row, piece_to_move.col), row, col) 
        is_check, attackers = temp_board.check_check(king_row, king_col, piece_to_move.color, BLKING)
        
        return is_check