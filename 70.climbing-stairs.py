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
Given problem, asks us to find the number of ways we can combine 1 and 2 to reach a given stair.

What defines a different way here?

1,2 is different from 2,1 so order of elements matter, permutations?

Find all ways? Recursion, DP?

direction?
We can begin at the end and work backwards.

Base case.
When we reach n = 0, we have reached final point.

we can build on this and find the num of ways to reach a positon beginning at n =1 or not take a step and begin from 0.

constraints,
    [1,45] pretty small

numWaysToClimbTo(n):
    if n == 0:
        return 1
    # now for cases where there is more than 1 stairs to climb.
    if n >1:
        twoStep = numWaysToClimbTo(n-2)
    oneStep = numWaysToClimbTo(n-1)
    return twoStep+oneStep
top down conversion
Bounds:
    n goes from n -> 0
    general value is dependent on smaller variables
    small before big.
    we iterate from 0 -> n.

    first replace numWaysToClimbTo with DP initiated to [0]*n+1.
    we take buffer of 1 value because stairs are 1 indexed and 0 signifies end.

    we then just loop from 0 to n where we directly use the logic of recursion.


"""
#@leet start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0]=1
        for i in range(0,n+1):
            if i > 1:
                dp[i] += dp[n-2]
            dp[i]+=dp[n-1]
        return dp[n]
            





        
# @leet end
