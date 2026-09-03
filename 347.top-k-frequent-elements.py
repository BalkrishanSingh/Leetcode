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
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [set()]
        hashmap = {}
        for i in nums:
            if i in hashmap:
                
                index = hashmap[i]-1
                if index < len(arr):
                    arr[index].remove(i)
                if index+1 < len(arr): 
                    arr[index+1].add(i)
                else:
                     arr.append(set([i,]))

                hashmap[i] += 1
            else:
                hashmap[i] = 1
                arr[0].add(i)
        result = []
        for i in range(len(arr) - 1, -1, -1):
            for num in arr[i]:
                result.append(num)
                if len(result) == k:
                    return result            
        return result
# @leet end
