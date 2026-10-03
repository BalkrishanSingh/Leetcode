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
Given a sorted array of size n that is rotated, lets say k times between 1 to n, we need to find the minimum in the array.
It can also be thought of that we need to find k%n as the minimum value should be at that index.

We are required to find a solution in logn time which suggests halving of work at each instance?
    Perhaps binary search is the key as it is a sorted array in the end..

Since we calculate compare 3 values in binary search, the left, right and mid.
Beginning with left at 0 and right at n-1.
    we calculate mid = left+(right-left)//2 at each step,
        if lets say, for example the mid is greater then the value at right, then we know that the lowest value should be somewhere to the right of mid,
        we increment left to mid+1
        otherwise we shrink right.
"""
# @leet start
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right =  len(nums)-1 
        while left < right:
            mid = left+ (right-left)//2 
            if nums[mid] > nums[right]:
                left = mid+1 
            else:
                right = mid
            
        return nums[left]


        
# @leet end
