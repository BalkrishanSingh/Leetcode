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
    LongestIncreasingSubsequenceEndingAt(i)


        max_len = 1, base case as there is always atleast one element in given array.
        We need to check going from 0 to i-1 with index called j, what is the length of the longest subsequence that ends at i:
        if arr[j] is less then arr[i] then it is valid to be included in the subsequence..
            if we find the LongestIncreasingSubsequenceEndingAt(j) and then compare it with max_len for each valid j,
            we can find the LongestIncreasingSubsequenceEndingAt(i).
        j is valid only and only if it is less than i.

        we need to loop over the result for all Subsequences that might end at that point instead of returning longest subsequences ending at n-1
        
        bounds:
        [0,nums(nums)-1]
        direction:
        j before i,
        smaller before bigger.
        0 to n

"""

# @leet start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LongestIncreasingSubsequenceEndingAt = [1]*(len(nums))
        for i in range(len(nums)):
            max_len = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    max_len = max(max_len,LongestIncreasingSubsequenceEndingAt[j]+1)
            LongestIncreasingSubsequenceEndingAt[i] = max_len 
        return max(LongestIncreasingSubsequenceEndingAt)
# @leet end
