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
for a given array of numbers T of size n, we need to find a result array also of size n where each element result[i] denotes the 
r-l+ 1 where r is the index of the next larger number after T[l] in T.
constraints are:
1,10e5. A nlogn or On solution required to avoid exceeding 10e10 

index values are small and between 30 and 70.

Same value in T doesnt satisfy the next larger number constraint.

atleast 1 value in T but then there is no greater integer for it.
If no future day is possible for a value, it needs to default to 0.
We can initiate result array itself to [0]*(len(T)) i suppose

we can use a monotonic stack to find next greatest element in On time

notes for later: In the focus on implementing monotonic stack, i forgot that I needed to return the distance and not the index of the next greater element

"""

# @leet start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*(len(temperatures))
        stack =[]
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                l = stack.pop()
                result[l] = i-l
            stack.append(i)
        
        return result
# @leet end
