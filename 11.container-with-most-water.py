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
For a given array of heights, we need to find the maximum water that can be occupied between two walls in this array,
Constraints:
    n:[2,10e5]
    height, [0,10e4]
The height of the pillars/walls inside any two walls we use is neglected,
    we can simply use the formula,

    min(left_max,right_max)*(right-left) to find the area. 
8721
8,
"""
# @leet start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1 
        while left < right: 
            if height[left] < height[right]:
                area = max(area,max(right-left,1)*min(height[left],height[right]))
                left +=1
            else:
                area = max(area,max(right-left,1)*min(height[left],height[right]))
                right -=1 
        return area


        
# @leet end
