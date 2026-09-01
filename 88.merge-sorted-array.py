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
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i: int = m -1
        j: int = n - 1
        k: int = m+n -1
    
        while k >=0 and (j>=0 and i>=0):
            if nums1[i]> nums2[j]:
                nums1[k] =nums1[i]
                i-=1
                k-=1
            elif nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j-=1
                k-=1
        while k >=0 and j>=0:
            nums1[k] = nums2[j]     
            j-=1
            k-=1
                
        while k >=0 and i>=0:
            nums1[k] =nums1[i]
            i-=1
            k-=1

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [4, 0, 0, 0, 0, 0]
    m = 1
    nums2 = [1,2,3,5,6]
    n = 5
    solution.merge(nums1, m, nums2, n)
    print(f"Test case 1: {nums1}")
# @leet end
