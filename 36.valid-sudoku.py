# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *
# @leet imports end
"""
For a given sudoko board represented as a list of lists of strings with each length 9 where each string is a digit from 1-9, we need to verify if it is a valid board.

A given board is valid if, All its column contain unique values between 1-9 or "." strings,

Similarly for rows and 3x3 sub box of the grind. Constraints given support this without any extra info.

The problem can be devided into 2 parts,

    first getting the list of elements in each different part to verify.
        
        Row: board[row]
        Column: [board[x][col] for x in range(9)]
        box: 
            for a given row and column, It can belong to 9 different sub boxes in the board,
                we can create a function to find the elements in a area of the board based on the index of the box.
                    
                    this should accept values from 0 to 2 for both idxs.
                    def getbox(rowidx, colidx): 
                        cells = []
                        for row in range(rowidx*3+3):
                            cells.extend(board[row][colidx*3:colidx*3+3])
                        return cells
                        
            
    For the found list, we need to check if it is valid, we can create a function for this task.
        def isvalid(cells):
            tracker ={}
            for cell in cells:
                if cell == ".":
                    continue
                if cell in tracker:
                    return false
                tracker.add(cell)

    Thirdly, we need to iterate over all the boxes, columns and rows and return False if any fails the validty check.
    otherwise at the end of the iterations, we can return True.



"""
# @leet start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def getBox(rowIdx, colIdx): 
            cells = []
            for row in range(rowIdx*3,rowIdx*3+3):
                cells.extend(board[row][colIdx*3:colIdx*3+3])
            return cells
                        
        def isValid(cells):

            tracker =set()
            for cell in cells:
                if cell == ".":
                    continue
                if cell in tracker:
                    return False
                tracker.add(cell)
            return True

        for row in range(9):
            if not isValid(board[row]):
                return False

        for col in range(9):
            if not isValid([board[x][col] for x in range(9)]):
                return False 

        for rowIdx in range(3):
            for colIdx in range(3):
                if not isValid(getBox(rowIdx,colIdx)):
                    return False 
        return True
# @leet end
