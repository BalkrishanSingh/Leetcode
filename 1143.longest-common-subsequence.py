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
For two given strings with length m and n, we need to find the longest subsequence shared between them.
As it is a subsequence, it doesnt need to be contigious but it needs to follow the sequence of the given strings.
If there is no subsequence we need to return 0.

Constraints, 
m:[1,1000]
n:[1,1000]
strings only consist of lowercase english letters.
A solution I can see involves the use of recursion where we have the following decisions to make.

For a given position in both i and j, the longest possible subsequence upto that point will be
    longestCommonSubsequenceByIndex(i,j)
        where the base case is:
            return 0 if either i or j is >= m and n respesctively

        next we for the current step, we see if the current indexes are same then we include it in the subsequence and increment both i and j
        if not matching we then check for maximimum of the longestCommonSubsequence if we skip ahead on i or j to match instead.

        A simple dry run.

        abcde ace
        i j current max
        0 0 1 + max(i+1,j and i,j+1)
        we check
            1 0 0 +
                2 0 

                1 1
                
            0 1 0 +
                1 1

                0 2
        and so on.

Recursive expression:
    
               






"""
# @leet start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        bounds:
        i: [0,len(text1)]
        j: [0,len(text2)]
        direction:
            general term i,j 
                Equal depends on i+1 and j+1 
                big before small.
                len(text1) before 0
                Continue ahead text1: i+1,j
                same
                Continue ahead text2: i,j+1
                same

        
            """
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for j in range(len(text2)-1,-1,-1):
            for i in range(len(text1)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1+ dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])


        return dp[0]0]
        
# @leet end
