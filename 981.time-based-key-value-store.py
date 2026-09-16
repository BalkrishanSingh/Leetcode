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

we need to create a custom class TimeMap that has the functions,
    set which adds a given key, value to a map with the given timestamp.
    get which given a key and a timestamp, finds the value with the largest from the set of timestamp <= timestamp.

    we could use a simple binary search to find the value that satisfies this constraint.
    or we could use bisect_right.

    while (left < right):
        mid = left + (right-left)//2
        if values[mid] <= target:
            left = mid + 1
        else:
            right = mid


"""

# @leet start
class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashMap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashMap.get(key,[])
        if values == []:
            return ""
        left = 0
        right = len(values)
        while left < right:
            mid =  left + (right-left)//2 
            if values[mid][0] <= timestamp:
                left = mid+1
            else:
                right = mid
        if left == 0:
            return ""
        return values[left-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @leet end
