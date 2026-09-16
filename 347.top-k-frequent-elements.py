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
given, a array and a integer k. we need to find the k most requent elements.

constraints: n: [1,10e5]
            nums[i]: [-10e4,10e4].

For this question, we could use a min heap with the pair (frequency, element) stored in the minheap,
where we first compute the frequency of all elements and store it in a hashmap beforer we proceed to make the minheap.
for each element as we traverse over the hashmap,we compare its frequency with the frequency of the element with the smallest fequency and replace it if bigger.
then we just use the minheap at the end with a list comprehension to only return the num values. This should be a nlogn solution.

we could also simplfy this and use heapq.nlargest() with the same list comprehension and zip function to simplfy.

We could also use a frequency indexed array of size, n+1 where 0th index represents elements with 0 frequency while the rest ith position index signify i frequency,
it will be a list of lists.


"""




# @leet start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}

        for num in nums:
            frequencyMap[num] = frequencyMap.get(num,0)+1
        buckets = [[] for _ in range(len(nums)+1)]

        for num,frequency in frequencyMap.items():
            buckets[frequency].append(num)
        res = []
        for idx in range(len(buckets)-1,-1,-1):
            for item in buckets[idx]:
                res.append(item)
                if len(res) == k:
                    return res
        return res
            
        # return [x[1] for x in heapq.nlargest(k,zip(frequencyMap.values(),frequencyMap.keys()))]

        

        
# @leet end
