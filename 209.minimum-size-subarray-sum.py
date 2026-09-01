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

# @leet start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left:int = 0
        right:int = 0
        sum:int =0
        min_len:int = 100000

        while right < len(nums):
            if sum < target:
                sum += nums[right]

            while sum >= target and left < len(nums):
                min_len = min(min_len,right - left +1)
                sum -=  nums[left]
                left += 1
            right +=1
                
        if min_len == 100000:
            return 0
        else:
            return  min_len




# Currently, The plan was to just go from left to right, dynamically modifying the sliding window based on if we are over the target or are under the target. We'd trim if we are over and we'd add if we are under.
# The plan was to just to store the minimum found length of the subarray as we go, looping over the entire input array,  Updating if we find another subarray which is smaller.



S = Solution()
print(S.minSubArrayLen( nums = [2,3,1,2,4,3], target = 7))
# @leet end
