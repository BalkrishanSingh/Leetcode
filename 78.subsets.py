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
for a given array, we need to find the power set, ie set of all subsets of a array.

a given array size is bounded between [1,10],
which is very small.

The values of num[i] is bounded between [-10,10]
which is also very small, negative and they are unique.

Unique is important as it simplifies the issue of having duplicate subsets,
all we need to consider is the indexes of the values themselves and avoid duplicating them..

We could use recursion to explore the entirety of the search space..
at each step,
    we either include a element,
    or we don't include it.

    But What do we return?
        Since this problem has a smaller bound, 
        we could simply use a external array and append to it when we hit the base case which is just i going past the last index of the array.
        this as such will be a n2^n solution because we are also copying the array, which for given 2^10 is doable..
    
    and what does including and not including actually imply..


Working of the solution I searched,
It keeps a result array like I did.

However it recurses differently,
Instead of a binary decision per recursion like I did, 
it explores the search space with a loop.
For each index in a loop, first the element is included and then we recurse and find and add all the subsets of nums that have that element,
then we pop it and then for the remainder of the loops, it is treated as if it wasn't added.

This repeats until we find all subsets.


"""

# @leet start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def powerset(i,arr):
            result.append(arr[:])
            for j in range(i,len(nums)):
                arr.append(nums[j])
                powerset(j+1,arr)
                arr.pop()
        powerset(0,[])      
        return result

# @leet end
