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
You are given an integer array cost where cost[i] is the cost of i^th step on a staircase.

Once you pay the cost, you can either climb one or two steps.
-- cost[i] gives the cost to go increment from i by one or two steps aka 
    -- current running cost is increased by cost[i]
    -- i is incremented by either 1 or 2 

You can either start from the step with index 0, or the step with index 1.
    -- we don't necessarily have to start from index 0 and accept the cost[0]
        -- we can potentially do 1-indexing where index 0 represents the index before the cost array starts
Return the minimum cost to reach the top of the staircase, which is the position just past the last step (index cost.length).
    -- we need to find the minimum to reach the top
        -- top  is defined as one step past the last index of I or cost.length
            -- with 1 indexing, that would be cost.length+1
        -- optimisation problem 
        
input constraints:
    cost.length: [2,1000] medium 
    cost[i]: [0,999] medium 
    cost length is large enough that we can't use backtracking to brute force a correct solution 
    the minimum length is 2 which is quite interesting as it means that we have to chose the optimum index to begin from each time 
    cost is positive, so no negative cost as such cost will either increase on moving forward or stay same.
    cost isn't unique

Decision:

    Example:
        cost = [10,15,20]
        we can start at either 0 or 1 
        i goes upto len(cost) as a constraint 
        i: [0,len(cost)]
        that is i:[0,3] 
        starting at i what are my actions,
            take cost[i] as my cost, (if i is less than len(cost))
            then increment i by 1
                make decision begnning at i+1
                with cost[i+1] fixed and actions: increment 1 or increment 2
            then increment i by 2 
                make decision begnning at i+2
                with cost[i+2] fixed and actions: increment 1 or increment 2 



                
-- recurrence relation is formed here as same structure is repeating
    base case:
        when i == len(cost),we return as 0 as we have reached the goal and we dont require any more cost. 
    parameters:
        affected parameter is i which gets incremented differently with different actions
    actions:
        increment i by 1 or 2 
    returned value: 
        ith_cost + min of the i+1thcost and i+2th cost 

Summary:
    We have to optimise to find the minimum cost to reach i = len(cost) 
    by chosing the correct step to increment from and where the cost[i] is the cost of incrementing from i by either 1 or 2 
    
conversion to topdown:

    bounds: 
        i:[0,len(cost)]
    direction?
        i+1 and i+2 before general term i
        big before small
        len(cost) before 0
"""
# @leet start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp_i1 = 0
        dp_i2 = 0
        for i in range(len(cost)-1,-1,-1):
            dp = cost[i] + min(dp_i1,dp_i2)
            dp_i2 = dp_i1
            dp_i1 = dp
        return min(dp_i1,dp_i2)

# @leet end
