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
given a 1-indexed array, we need to return the index of two numbers that add upto a given target number using constant space without reusing element twice,
a element is distinguished here by their index, not their value.

constraints suggest a N^2 solution will pass but we should be able to easily do it in O(N) with two pointers as the given array is sorted.

""""
# @leet start
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right =len(numbers)-1
        while left < right:
            ans= numbers[left]+numbers[right]
            if ans == target:
                return [left+1,right+1]
            elif ans > target:
                right -=1
            else:
                left +=1
        
# @leet end
