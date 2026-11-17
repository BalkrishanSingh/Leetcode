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
Given a array of unique numbers, we need to find all possible subsets.
a subset is defined as a set that is inside a set.

for backtracking, we iterate over the entire array while recursing, iteration allows us to avoid using duplicates of a single index.

we use a single result array for returning.

we define a recursive function with index of current element,path as input ,
    where inside 
        for every index after the given input index in a loop,
            we first include and recurse 
        then we pop and recurse. 



"""

# @leet start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result =[]
        def subsets(idx,subset):
            result.append(list(subset))
            for i in range(idx,len(nums)):
                subset.append(nums[i])
                subsets(i+1,subset)
                subset.pop()
        subsets(0,[])
        return result
        
        
# @leet end
