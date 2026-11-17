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
"""Given a array of numbers, we need to find a array of numbers where each number is equal to the product of all numbers except that index

given constraint is, n :[2,10e5] so we need a solution faster than N^2 and the problem itself specifies finding a O(n) solution.

a given number could be 0 so we can't simply use a running product and divide by the current value.

for a brute force solution, it would be to iterate over every element, keeping a running product of the previous elements and then scan into the future with a for loop to find the suffix product of that and then multiply the prefix and suffix.

Since the prefix and sufix for a given index are constant, we don't need to compute them again and again in a nested for loop.

we could simply use a simple for loop before the main answer computation to find the prefix and suffix products of each index.

this does take 2N space extra space and the solution asked if we can do it in O(1) space.
 
My initial thought took me to using 2 pointers with a running prefix and suffix but we need the entire suffix or prefix, 
    if we increment left in fixed manner, prefix isnt a issue 
    but for suffix, we need to compute the entire suffix of a element 
    and for the next element to the right, we can't just divide to obtain that suffix because it is possible we have 0 numbers or we need to compute it on the spot,
    both either compromises on the answer or the time complexity but we do reduce space complexity from 2N to N.

Oh wait, we don't really have to create the result in a single pass and speaking of N space, 
we have it in the result array.
since we have to multiply those index at the end anyways, we can just first treat the result array to store prefix and as we compute suffixes, we can directly just compute result as we go in another pass.
it lowers time complexity from 3n to 2n and removes extra space usage.



"""
# @leet start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [None]*(len(nums)+1)
        prefix = 1
        for i,num in enumerate(nums):
            result[i] = prefix
            prefix *= num
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= suffix
            suffix += nums[i]


        return result

# @leet end
