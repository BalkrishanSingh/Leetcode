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
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left:int = 0
        right:int = len(numbers) -1

        while left < right:
            if target - numbers[right] == numbers[left]:
                return [left+1,right+1]
            if target - numbers[right] > numbers[left]:
                left +=1
            else:
                right -=1
        return [-1,-1] # if there is no two sum
            
S = Solution()
print(S.twoSum( numbers = [2,3,4], target = 6))
# @leet end
