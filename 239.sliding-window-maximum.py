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

You are given an array of integers nums, 
it is 1 to 10e5 in size which is quite large and as such the solution should be O(n) or O(nlogn)


there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. 

sliding window but there are negative numbers in the array..

Each time the sliding window moves right by one position. Return the max sliding window.
Based on the example, the returning value is a array of the maximums in each sliding window.

basically we have to find the maxiumum in each given sliding window of a array, add it to a result array and return that array.

Main restriction should be in optimisation as a simple bruteforce solution should be to seperately find max on each of the sliding window,
it would be a slow solution around O(K*(N-K-1)) which seems to time out on implentation as I thought.
left = 0
    right = k 
    result = []
    while right <= len(nums):
        result.append(max(nums[left:right]))
        left += 1 
        right += 1
    return result
Perhaps we could use a max heap of size k where I append the new element each time and pop the oldest one at the same time and then sort and return?
It would be worse time complexity than just using max operation as we have to linearly search and remove the last element, add a new element which is O((k+logk+1)*(N-K-1))

we can consider a monotonic Deque where left elements slide out as we go by getting popped each loop
and following the principles of monotonic stack where we keep remove the right element if it is smaller then the current new element repeatedly until all are removed or we find a greater value which will be stored at the front.

we return this front value and each loop we check if its in the range of the allowed sliding window by i-k+1 which is just a simple algebric transofmration of i-j+1 = k

either way, we have to use O(n) space complexity for k = 1 where every item is a maximum and needs to be returned


"""
# @leet start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = Deque()
        result = []
        for i in range(len(nums)):
            if dq and dq[0] < i - k +1:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result

# @leet end
