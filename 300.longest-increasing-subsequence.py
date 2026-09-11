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
Given an integer array nums,  
return the length of the longest strictly increasing subsequence.

Subsequence: It implies that it has to be in order and is not required to be contigious 
Strictly Increasing, Equal values are not valid to be in the subsequence.

 Constraints:

	* 1 <= nums.length <= 2500
	Let n = nums.length,
        n is always atleast 1 so the length of the minimum subsequence we can return is 1,
        n's largest value is medium.

	* -10^4 <= nums[i] <= 10^4
    The individual value of nums[i] is large in size and can be negative..

Order:
    If we traverse left to right, we will be finding the increasing sequence.
    right to left traversal is possible but we got to find the decreasing sequence instead.

Patterns:
    it seems to be a DP problem based on subsequences..

Decision:
    beginning at index 1, what are my actions.
    Include element 1 in sequence 
        consequences:
            I can only take a value greater than element 1. I need to somehow keep the previous element 
        contribution:
            +1 to the length of the sequence.
        affected variable:
            1 increases to 2
            we repeat decision,
                include 2

                not include 2

    do not include element 1 in sequence.
        consequences:
            no consequences
        contribution:
            no contribution
        affected variable:
            1 still increases by 1 
            we repeat decision.
                include 2
                not include 2..
    base case:
        if i >= n:
            return 0..
    
    recurrence relation.
    dp(i,largest):
        if i>= n:
            return 0
        included = 0
        if arr[i] > largest:
            included =  1+ dp(i+1,arr[i])
        not_included = dp(i+1,largest)
        return max(included,not_included)

     

"""

# @leet start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dp(i,largest):
            if i>= len(nums):
                return 0
            included = 0
            if nums[i] > largest:
                included =  1+ dp(i+1,nums[i])
            not_included = dp(i+1,largest)
            return max(included,not_included)
        return dp(0,-(10e4+1))

# @leet end
