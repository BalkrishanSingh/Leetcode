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

For a given array of non overlapping intervals, we need to insert a new interval and resolve and remove overlap and return the new array.

the length of intervals array is 10e4 at maximum and 0 at minimum. We are always given a new interval to add.
Intervals is sorted in ascending order based on the start of the intervals, and are guaranteed to be non overlapping.

We could simply transfer the intervals that have their end before the start of the new interval and directly add it onto the resulting array.

then for any interval in intervals that overlap with the new interval, we need to repeatedly merge.
    


once we get to the interals that have their start times after the new interval end times, we can just directly append them all to result.


We could have also just mathematically inserted the new interval into the array with binary search perhaps and then merged intervals across the array.

"""    
# @leet start
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        idx = 0
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            result.append(intervals[idx])
            idx +=1 
        result.append(newInterval)
        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            result[-1] = [min(result[-1][0],intervals[idx][0]),max(result[-1][1],intervals[idx][1])]
            idx+=1
            
        while idx < len(intervals) and intervals[idx][0] > newInterval[1]:
            result.append(intervals[idx])
            idx+=1 
        return result
        


# @leet end
