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
Summary, For a given string. we need to find the longest substring in the string that has no duplicate characters.
we can use sliding window approach as this problem is monotonic in nature. Increasing the sliding window size will never decrease the size of the window. It will only make it invalid and thus require shrinkage.
We can use a simple hash set to see if a char is in the map or not, if it is we can repeatedly shrink until the current slding window is valid again then updat the max size

"""
    
# @leet start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        maxSize = 0
        left = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                if s[left] in seen:
                    seen.remove(s[left])
                left +=1 
            seen.add(s[right])
            maxSize = max(maxSize,right-left+1)
        return maxSize 
            


        
# @leet end
