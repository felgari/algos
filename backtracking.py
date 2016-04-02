#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Felipe Gallego. All rights reserved.
#
# This is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Algorithms using backtracking.
"""

import sys

NUM_ARGS = 2
MIN_SIZE = 3
QUEEN_BOARD_SIZE = 8
SUDOKU_BOARD_SIZE = 9
QUEEN_VAL = True 
NO_QUEEN_VAL = False
QUEEN_STR_VAL = '*' 
NO_QUEEN_STR_VAL = 'O'

def factorial(size):
    
    if size == 1:
        return 1
    else:
        return size * fibonacci(size - 1) 
    
def fibonacci(size):
    
    if size <= 1:
        return 1
    else:
        return fibonacci(size - 1) + fibonacci(size - 2)

class QueensBoard(object):
    
    def __init__(self):
        
        self._board = [[ NO_QUEEN_VAL for _ in range(QUEEN_BOARD_SIZE)] 
                for _ in range(QUEEN_BOARD_SIZE)]
        
        self._queens_row = [ -1 for _ in range(QUEEN_BOARD_SIZE) ]
        
    def cell_valid_for_queen(self, row, col):
    
        if row < 0 or row >= QUEEN_BOARD_SIZE or \
            col < 0 or col >= QUEEN_BOARD_SIZE:
            return False
        
        queen_found = False
    
        # Look for queens in this row in previous columns.
        j = 0
        while not queen_found and j < col:
            if self._board[row][j] == QUEEN_VAL:
                queen_found = True
            j += 1
        
        # Look for queens in previous columns in diagonals to the left.
        j = col - 1
        h = 1
        while not queen_found and j >= 0:
            i_up = row - h
            if i_up >= 0:
                if self._board[i_up][j] == QUEEN_VAL:
                    queen_found = True
            i_down = row + h
            if (not queen_found) and i_down < QUEEN_BOARD_SIZE:
                if self._board[i_down][j] == QUEEN_VAL:
                    queen_found = True
            h += 1
            j -= 1
        
        return not queen_found 
    
    def find_queen_row(self, col):
        
        return self._queens_row[col]
    
    def set_queen(self, row, col):
        
        self._queens_row[col] = row
        
        self._board[row][col] = QUEEN_VAL
        
    def remove_queen(self, row, col):
        
        self._queens_row[col] = -1        
        
        self._board[row][col] = NO_QUEEN_VAL     
        
    def previous_cell_to_try(self, prev_col):
        
        row_prev_col = self.find_queen_row(prev_col)
        
        # Remove the queen from this position.
        self.remove_queen(row_prev_col, prev_col)
        
        # Check the row in the previous columns isn't the last one.
        if self.is_last_row(row_prev_col):
            prev_col -= 1
            
            if prev_col >= 0:
                row_prev_col = self.find_queen_row(prev_col)
                self.remove_queen(row_prev_col, prev_col)
            else:
                print "ERROR: no column to use, this shouldn't happen!!!"
                sys.exit(-1)
            
        # At this point the row found cannot be the last of the column.
        new_row = row_prev_col + 1 
        
        return new_row, prev_col       
        
    def is_last_col(self, col):
         return col == QUEEN_BOARD_SIZE -1  
     
    def is_last_row(self, row):
         return row == QUEEN_BOARD_SIZE -1      
        
    def __str__(self):
        
        str_board = [[ NO_QUEEN_STR_VAL for _ in range(QUEEN_BOARD_SIZE)] 
                    for _ in range(QUEEN_BOARD_SIZE)]
        
        for i in range(QUEEN_BOARD_SIZE):
            for j in range(QUEEN_BOARD_SIZE):
                if self._board[i][j] == QUEEN_VAL:
                    str_board[i][j] = QUEEN_STR_VAL
        
        str_list = []
        
        for sb in str_board:
            str_list.append(' ' .join(sb))   
            
        return '\n'.join(str_list)                    

def eiqht_queens(board, cur_row, cur_col):
    
    # Check if current position is valid for a queen. 
    if board.cell_valid_for_queen(cur_row, cur_col):

        board.set_queen(cur_row, cur_col)
        
        if board.is_last_col(cur_col):
            # Finished!!
            print board  
        else:    
            # A queen for the next column.
            eiqht_queens(board, 0, cur_col + 1)
            
    # Current position is not valid and current row isn't the last one in 
    # current column.
    elif not board.is_last_row(cur_row):
        # Try the next row in current column.
        eiqht_queens(board, cur_row + 1, cur_col)
        
    # There is not any cell available in this column.
    else:
        # Try a new position in a previous column.
        new_row, new_col = board.previous_cell_to_try(cur_col - 1)      
            
        eiqht_queens(board, new_row, new_col)                    
            
def resolve_eight_queens():
    
    print "Eight queens:"
    board = QueensBoard()
    
    eiqht_queens(board, 0, 0)    
    
def init_sudoku_board():

    board = [[ 0 for _ in range(SUDOKU_BOARD_SIZE)] \
                for _ in range(SUDOKU_BOARD_SIZE)]
    
    return board
    
def resolve_sudoku():
    
    board = init_sudoku_board()
    
    print "Sudoku pending"

def main(size):
    
    print "Factorial of %d is: %d" % (size, factorial(size))
    
    print "Fibonacci of %d is: %d" % (size, fibonacci(size))       
    
    resolve_eight_queens()
    
    resolve_sudoku()    
    
    return 0

if __name__ == "__main__":
    
    if len(sys.argv) != NUM_ARGS:
        print"ERROR: Falta argumento. Uso: %s size" % sys.argv[0]
    else:
        size = int(sys.argv[1])
        
        if size >= MIN_SIZE:
            sys.exit(main(size))
        else:    
            print "Size must be at least %d" % MIN_SIZE