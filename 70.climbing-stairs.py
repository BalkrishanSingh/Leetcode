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

#You are climbing a staircase. It takes n steps to reach the top.
#   takes n  steps
#       - goal: n
#           - we stop at goal, we can't go past it 
#               - that constraints the steps we can take near the goal 
#   climbing from ground to top 
#       it will proceed from 0 to n
#
# each time you can either climb 1 or 2 steps.
#  -allowed incremenet value 
#       -1 
#       -2 
#
#
# in how many distinct ways can you climb to the top?
#       -counting problem where we find number of ways to reach top 
#       - it doesnt care about duplicates
#           i.e. 1+2 and 2+1 are two different valid answers
#
# 
# we need to find the distinct number of ways that values 1 or 2 sum up to n
#   distinct: 
#       distinct is a little uncertain as we can use the same steps in different order
#       and it will be valid answer
#
# input constraint:
#   n: small 
#   bound: [1,45]
#   positive and non zero
#       no negative steps required
#       no zero step answer as at minimum 1 step required
#       the remainingSteps will always decrease
# decision:
#   simulation:
#      for remainingSteps = n, we can take two actions initially
#           take 1 step:
#               remainingSteps required = remaining steps  - 1
#               
#               take 1 step:
#                   remainingSteps = remainingSteps - 1 = 0. [constraints: 1 <= remainingSteps]
#               take 2 step: 
#                   remainingSteps = remainingSteps - 2 = 0 [ constraints: 2 <= remainingSteps]
#           take 2 step:
#               remainingSteps = remainingSteps - 2 = 0 [ constraints: 2 <= remainingSteps]
#                    take 1 step:
#                   remainingSteps = remainingSteps - 1 = 0. [constraints: 1 <= remainingSteps]
#               take 2 step: 
#                   remainingSteps = remainingSteps - 2 = 0 [ constraints: 2 <= remainingSteps]
#
#           we are repeating exact same logic after a single step?
#               recurrence relation..
#                   dependent variable? 
#                       remainingSteps 
#
#                   posible action?
#                       take 1 step or 2 step, both constrained by the remainingSteps being greater or equal then the step
#                   
#                   time and space complexity?
#                       catched complexity should be O(1) as there is no loops in the action and it is simple decrement 
#                       there is one parameter so O(n) for time complexity
#                   base case? 
#                       when does it stop?
#                           when remainingSteps is 0
#                       what does it return?
#                           it should return 1 as it will be a distinct way to reach n 
#
"""
            bounds: 
                n: [0,n or 45]
                direction?
                    term n required
                    take 1 step:
                        n-1 before n
                        small before big 
                    take 2 step:
                        n-2 before n
                        small before big
                        0 before n
                dp array dimensions  = 1D as only 1 parameter
"""
#@leet start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp_1 = 0
        dp_2 = 0
        for x in range(n+1):
            if x == 0:
                waysThatReachedStep = 1
            else:
                waysThatReachedStep = dp_1
                if 2 <= x:
                    waysThatReachedStep += dp_2
            dp_2 = dp_1
            dp_1 = waysThatReachedStep
        return dp_1
  
# @leet end
