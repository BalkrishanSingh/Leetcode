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
For a given problem, we need to find the longest increasing subsequence of a array.

A subsequence of a array is a non contigious but in order series of element of a array, a subsequence can have 0 and more elements and be the entire array.


Constraints:
nums.length: [1,2500]
nums[i]: [-10e4,10e4]

We should be able to use a solution with higher complexity, the statement of the solution also suggests that a worse solution than nLogn is acceptable.

Considerations:
    
    any element can be thought of as the start of a susbsequence so the base case for the longest icnreasing subsequence should be 1 as the minimum input is also 1 in length.

    def LongestSubsequenceThatEndsAt(i):
        max_len = 1
        for idx in range(i):
            if arr[idx] < arr[i]:
                max_len = max(max_len, LongestSubsequenceThatEndsAt(idx)) +1
        return max_len
    the time complexity should be N^2 due to the use of a for loop for a 1-D problem 
    space complexity is still N.

    for actually finding the end answer, we need to conser the fact that a longest sequence could end at any point in the array and not be constrainted.
    so we need to find the max of the LongestSubsequenceThatEndsAt over the entire list indexs.

    we should also consider the conversion to top down for efficieny.

    we can convert it to topdown by first replacing LongestSubsequenceThatEndsAt with DP that is initialised to [1]*n where n is length of arr.
    
    then we just need to run a loop from 0 to i as we had already done for the recursion and then just do the function call where the recurrsive calls are replaced with DP accesses, max_len is replaced by usage of DP[i]

    we can then replace the function call with the for loop.

       
"""

# @leet start
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1]*n 
        result = 1
        for i in range(n):
            for idx in range(i):
                if nums[idx]< nums[i]:
                    dp[i] = max(dp[i],dp[idx]+1)
            result = max(dp[i],result)
        return result


        
# @leet end
