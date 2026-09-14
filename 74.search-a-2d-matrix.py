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
You are given an m x n integer matrix matrix with the following two properties:

	* Each row is sorted in non-decreasing order.
	
	* The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Given a sorted matrix, we need to find if a target value is present in the array or not.
    
constraints, matrix can contain negative values [-10e4,10e4] and m and n are bounded by [1,100]

    Since we need to find it in log(m*n), we could use binary search since it is in logarithmic time..
        We could flatten the m*n matrix into a 1D array preemptively or index it with a single value by using some math.
            for i,j = 1,2
                we could convert it to a single index by using idx=m*1+2
                1*3+2
                (idx//m) (idx%n)


"""

# @leet start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)*len(matrix[0])-1
        while left <= right:
            mid = left + (right-left)//2
            i,j = mid//len(matrix[0]), mid%len(matrix[0])
            midVal = matrix[i][j]
            if midVal == target:
                return True
            elif midVal < target:
                left = mid +1
            else:
                right = mid-1
        return False
# @leet end
