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
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2 
            if nums[mid] == target:
                result = mid
                break 
            elif nums[mid] < target:
                left = mid +1 
            else:
                right = mid - 1
        return result
        
# @leet end
