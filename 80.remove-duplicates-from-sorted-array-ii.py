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
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return
        j: int = 2
        for item in nums[2:]:
            if nums[j-2] != item:
                nums[j] = item
                j+=1
        return j
        
if __name__ == "__main__":
    solution = Solution()
    
    def run_test(test_name, nums, expected_k, expected_nums):
        original_nums = nums.copy()
        
        # Edge case for empty array that might break the user's logic
        # if the user hasn't handled it yet.
        try:
            k = solution.removeDuplicates(nums)
        except Exception as e:
            print(f" {test_name} failed with Exception: {e}")
            print(f"   Original nums: {original_nums}")
            return
            
        try:
            assert k == expected_k, f"Expected length {expected_k}, got {k}"
            # The problem states the first k elements of nums should contain the result
            actual_nums = nums[:k]
            assert actual_nums == expected_nums, f"Expected elements {expected_nums}, got {actual_nums}"
            print(f"{test_name} passed!")
        except AssertionError as e:
            print(f" {test_name} failed: {e}")
            print(f"   Original nums: {original_nums}")

    # Provided test case
    run_test("Test Case 1", [0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3])
    
    # Standard test case
    # run_test("Test Case 2", [1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3])
    
    # Other potential cases for problem 80
    # run_test("Empty Array", [], 0, [])
    # run_test("All Elements Match", [2, 2, 2, 2], 2, [2, 2])
    # run_test("No Elements Match", [1, 2, 3], 3, [1, 2, 3])
    # run_test("Single Element", [1], 1, [1])
# @leet end
