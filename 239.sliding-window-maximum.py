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
Summary:
for a given array and a number k which represent the size of a sliding window, 
we need to find the maximum of each sliding window as we move the sliding window left to right in the given array.
We can simply use list slicing and max function to iterate over the array and find the max from each sliding window.

We could also implement a monotonic deque, which will store the indexes of the given array
    
we use a while loop to iterate through the array
    At each step, we check if dq isnt empty

    if the left most element of deque is less than i-(k-1), we pop repeatedly until it isnt.

    then addition of new element while maintaining monotonic property.
        to maintain this property, we compare the right most element of the dq and repeatedly pop if it is smaller then current element.
    append current element.

    then we append left most element of the dq to array once.
        only and only if i >= k-1






"""
# @leet start
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        dq = deque()
        for i in range(len(nums)):
            while dq and dq[0] < i-(k-1):
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                result.append(nums[dq[0]])
        return result
        
# @leet end
