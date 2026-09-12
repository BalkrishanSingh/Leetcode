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
given question asks us to find the longest strictly increasing subsequence of a given array,
and return it's length.

the size of the given array is bounded between [1,2500] which is medium
values of the nums[i] themselves is bounded between [-10e4,10e4].

Direction, 
We could proceed from 
    left to right
        need to see if i value < r value or not
    right to left
        will be the same but in reverse order ig..

pattern,
    It seems like a subsequence dp problem? We just need to optimise for the longest length 
    with the constraint of previous element being greater than the current one...

decision:
    LongestSubsequenceThatEndsAt(4):
        
        If we fix the element which is included in the subsequence,
            we just need to compare with the values of all the element preceeding it,
                then if they are smaller than it then they could be part of it's longest sequence,
                to truly check the maximum, we just compare the max_len found so far..
            max
            for i from 0 to 3:
                if i less than 4:
                    then max(LongestSubsequenceThatEndsAt(i)+1,max).
            then we just return this max..

        since we are fixing the last value included in the array with this recursive function
        and the subsequence could actually end anywhere in the array,
        we need to use a loop to find the maximum subsequence that ends at any point in the array..

        since a solution i is dependent on values smaller than it,

        if we convert this solution to top down, the for loop should go from 0 to n.

        
        we could also use the princple of binary search to effectively find the longest subsequence,
        at every step, if a value is smaller then any the values present already in a array, 
        then we replace it at that point by using bisect_left..

        if not, we append it since it will form a increasng sequnce with the previous values already..

        for example,  0,3.
        with bisect left on this array with value 2. It gives the value 1.

        while left < right:
            mid = (left+right)//2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid+1
        return left
            

        
"""

# @leet start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        patience_sort = []
        for i in range(len(nums)):
            idx = bisect_left(patience_sort, nums[i])
            if idx == len(patience_sort):
                patience_sort.append(nums[i])
            else:
                patience_sort[idx] = nums[i]

        return len(patience_sort)
            
                    

        
# @leet end
