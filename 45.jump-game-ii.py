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
    def jump(self, nums: List[int]) -> int:
        dp = [-1 for x in range(len(nums))]
        dp[0] = 0
        farthest_point = 0
        last_jump_point = 0

        for i, distance in enumerate(nums):
            if i <= farthest_point:
                if dp[i] == -1:
                    dp[i] = 1 + dp[last_jump_point]
                else:
                    dp[i] = min(dp[i],dp[last_jump_point] + 1)
                if farthest_point < i + distance:
                    farthest_point = distance +i
                    last_jump_point = i
        return dp[len(nums) -1] 
            
# in the process of optimising for time, we are only doing a single pass. 
# This is leading to a issue in the current solution such that
# for a case such as [2,3,1] We overwrite the farthest distance and last jumping point we can go as we find a new further point even when unnecessary, leading us to take extra steps.
# Ideally, we'd wait to assign the last jumping point until we know for sure it's the last point.
# If we delay it assigning however, we may run into issues such as a farthest point being found earlier. 
if __name__ == "__main__":
    solver = Solution()
    result = solver.jump([2,3,1])
    print(f"Input: [2,3,1] | Expected: 1 | Actual: {result} | {'PASS' if result == 1 else 'FAIL'}")
# @leet end
