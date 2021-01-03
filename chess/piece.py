import pygame
from .constants import SQUARE_SIZE, COLS, BLACK, ROWS, WHQUEN, BLQUEN, BLROOK, WHROOK

class Piece:
    def __init__(self, row, col, color, image):
        self.row = row
        self.col = col
        self.color =color
        self.image = image
        self.x, self.y = 0,0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE//2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE//2
    
    def draw(self, win):
       win.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2) ) 
       #this puts the image in place at the certain x and y location the piece has. Have to recenter the image by getting the midpoint
       #not all images are uniform
    
    def get_valid_moves(self):
        pass

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
    
    def change_queen(self, board):
        pass


class King(Piece):
    def __init__(self,row,col, color, image):
        self.row = row
        self.col = col
        self.color = color
        self.image = image
        self.moved = False
        self.x , self.y = 0, 0
        self.calc_pos()

    def move(self,row,col):
        self.row = row
        self.col = col
        self.calc_pos()
        self.moved = True

    def get_valid_moves(self, board):
        moves = {}
        
        for row in range(3):
            for col in range(3):
                newR = self.row-1+row
                newC = self.col - 1+col
                if 0<= newR < ROWS and 0 <= newC < COLS:
                    if board.board[newR][newC] != 0:
                        if board.board[newR][newC].color != self.color:
                            moves[(newR,newC)] = [board.board[newR][newC]  ]  
                    else:
                        moves[(newR,newC)] = []

        moves.update(self.castle(board))
        return moves
    
    def castle(self,board):
        moves = {}
        if not self.moved:
            right = COLS-1
            left = 0
            if isinstance(board.board[self.row][left], Rook):
                allEmpty = True
                for i in range(3):
                    if board.board[self.row][self.col-1-i] != 0:
                        allEmpty = False
                if allEmpty:
                    if self.color == BLACK:
                        img = BLROOK
                    else:
                        img = WHROOK
                    moves[(self.row,self.col-2)] = [board.board[self.row][left], Rook(self.row, self.col-1, self.color,img )] #remove the rook, but then add in a new one in the right place
            if isinstance(board.board[self.row][right], Rook):
                allEmpty = True
                for i in range(2):
                    if board.board[self.row][self.col+1+i] != 0:
                        allEmpty = False
                if allEmpty:
                    if self.color == BLACK:
                        img = BLROOK
                    else:
                        img = WHROOK
                    moves[(self.row,self.col+2)] = [board.board[self.row][right], Rook(self.row, self.col+1, self.color, img)]

        return moves


class Knight(Piece):
    def get_valid_moves(self, board):
        moves = {}
        for i in range(2):
            adder2 = 2 * (-1)**i
            new_c = self.col +adder2 #left 2 or right 2. initial run right two
            if 0 <= new_c < COLS:
                for j in range(2):
                    adder1 = 1 * (-1)**j
                    new_r = self.row + adder1
                    if 0 <= new_r < ROWS:
                        if board.board[new_r][new_c] != 0:
                            if board.board[new_r][new_c].color != self.color:
                                moves[(new_r,new_c)] = [board.board[new_r][new_c]]
                        else:
                            moves[(new_r,new_c)] = []
            new_r = self.row + adder2
            if 0 <= new_r < ROWS:
                for j in range(2):
                    adder1 = 1 * (-1)**j
                    new_c = self.col + adder1
                    if 0 <= new_c and new_c < COLS:
                        if board.board[new_r][new_c] != 0:
                            if board.board[new_r][new_c].color != self.color:
                                moves[(new_r,new_c)] = [board.board[new_r][new_c]]
                        else:
                            moves[(new_r,new_c)] = []
        return moves


class Rook(Piece):
    def __init__(self, row, col, color, image):
        self.row = row
        self.col = col 
        self.color = color
        self.image = image
        self.moved =False
        self.x,self.y = 0,0
        self.calc_pos()

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
        self.moved = True

    def get_valid_moves(self, board):
        moves = {}
        search_left = True
        search_right = True
        search_up = True
        search_down = True
        up = self.row-1
        down = self.row+1
        left = self.col -1
        right = self.col+1
        while search_left or search_right or search_up or search_down:
            if left >= 0:
                if board.board[self.row][left] != 0:
                    if board.board[self.row][left].color != self.color:
                        moves[(self.row,left)] = [board.board[self.row][left]]
                    search_left = False
                else:
                    moves[(self.row,left)] = []
                    left -= 1
            else:
                search_left = False
            if right < COLS:
                if board.board[self.row][right] != 0:
                    if board.board[self.row][right].color != self.color:
                        moves[(self.row,right)] = [board.board[self.row][right]]
                    search_right = False
                else:
                    moves[(self.row,right)] = []
                    right += 1
            else:
                search_right = False
            if up >= 0:
                if board.board[up][self.col] != 0:
                    if board.board[up][self.col].color != self.color:
                        moves[(up,self.col)] = [board.board[up][self.col]]
                    search_up = False
                else:
                    moves[(up, self.col)] = []
                    up -= 1
            else:
                search_up = False
            if down < ROWS:
                if board.board[down][self.col] != 0:
                    if board.board[down][self.col].color != self.color:
                        moves[(down,self.col)] = [board.board[down][self.col]]
                    search_down = False
                else:
                    moves[(down,self.col)] = []
                    down += 1
            else:
                search_down = False
        return moves


class Bishop(Piece):
    def get_valid_moves(self,board):
        moves = {}
        search_45 = True#degrees
        search_135 = True
        search_225 = True
        search_315 = True
        counter1 = 1 #will go off in the directions 45, 135, 225, 315 degrees, respectively
        counter2 = 1
        counter3 = 1
        counter4 = 1

        #45 degrees, row -= 1, col += 1
        while search_45 or search_135 or search_225 or search_315:
            new_r = self.row-counter1
            new_c = self.col+counter1
            if new_r >= 0 and new_c < COLS:
                if board.board[new_r][new_c] != 0:
                    if board.board[new_r][new_c].color != self.color:
                        moves[(new_r,new_c)] = [board.board[new_r][new_c]]
                    search_45 = False
                else:
                    moves[(new_r,new_c)] = []
                    counter1 += 1
            else:
                search_45 = False
            
            #135 degrees, row+= 1 col += 1
            new_r = self.row+counter2
            new_c = self.col+counter2 
            if new_r < ROWS and new_c < COLS:
                if board.board[new_r][new_c] != 0:
                    if board.board[new_r][new_c].color != self.color:
                        moves[(new_r,new_c)] = [board.board[new_r][new_c]]
                    search_135 = False
                else:
                    moves[(new_r,new_c)] = []
                    counter2 += 1                
            else:
                search_135 = False
            
            #225 degrees, row += 1, col -= 1
            new_r = self.row + counter3
            new_c = self.col - counter3
            if new_r < ROWS and new_c  >= 0:
                if board.board[new_r][new_c] != 0:
                    if board.board[new_r][new_c].color != self.color:
                        moves[(new_r,new_c)] = [board.board[new_r][new_c]]
                    search_225 = False
                else:
                    moves[(new_r,new_c)] = []
                    counter3 += 1             
            else:
                search_225 = False

            #315 degrees, row -= 1, col -=1
            new_r = self.row - counter4
            new_c = self.col - counter4
            if new_r >= 0 and new_c >= 0:
                if board.board[new_r][new_c] != 0:
                    if board.board[new_r][new_c].color != self.color:
                        moves[(new_r,new_c)] = [board.board[new_r][new_c]]
                    search_315 = False
                else:
                    moves[(new_r,new_c)] = []
                    counter4 += 1  
            else:
                search_315 = False
        return moves


class Queen(Piece):
    def get_valid_moves(self, board):
        moves = {}
        moves.update(Bishop(self.row,self.col,self.color,self.image).get_valid_moves(board))
        moves.update(Rook(self.row,self.col,self.color,self.image).get_valid_moves(board))
        return moves

class Pawn(Piece):
    def __init__(self, row, col, color, image):
        self.row = row
        self.col = col 
        self.color = color
        self.image = image
        self.moved =False
        self.x,self.y = 0,0
        self.calc_pos()
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
        self.moved = True

    def change_queen(self, board):
        if self.row == 0  or self.row == 7:
            row =self.row
            col = self.col
            color = self.color
            board.remove(self)
            if color == BLACK:
                image = BLQUEN
            else:
                image = WHQUEN
            board.board[row][col] = Queen(row,col,color,image)
    
    def get_valid_moves(self, board): #where can this piece go?
        #note, board here must call board.board[i][j] to access a piece
        moves = {} 
        direction = 0
        check  = False
        if self.color == BLACK:
            direction = 1
        else:
            direction = -1

        for i in range(3):
            newCol = self.col - 1 + i
            if (0 <= newCol <=(COLS-1)):
                piece = board.board[self.row+1*direction][newCol]
                if newCol != self.col:
                    if piece != 0 and piece.color != self.color:
                        moves[(self.row+1*direction, newCol)] = [piece]
                        #CHECK if its a king maybe. But we have to look after the piece is placed
                else:
                    if piece == 0:
                        moves[(self.row+1*direction, newCol)] = []
        if not self.moved: #this accounts for the fact that a pawn can move 2 only if they have not moved yet
            if board.board[self.row+1*direction][self.col] == 0:
                piece = board.board[self.row+2*direction][self.col]
                if piece == 0:
                    moves[(self.row+2*direction, self.col)] = []     
        return moves
