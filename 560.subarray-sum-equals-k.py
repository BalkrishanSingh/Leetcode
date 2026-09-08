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
Given an array of integers nums and an integer k, 
return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

    so basically we have to find the number of different arrays that add up to a given k
    we seem to distingush between different subarrays by the index rather then values
    as 1,1,1 for k = 2 has 1,1 and 1,1 answers possible, beginning at 0 and 1 index.

    the constraints are num.length is 2*10e4 which is large and there is always atleast 1 element 
    value of nums themselves can be negative and is between -1k to 1k which is medium
    the value of k itself is 10e7 which is quite large and can be negative.

    negative values complicates thing as we can't naively use sliding window as the sum doesn't monotonically increase with the size of the sliding window..
    subarray is contigious and non-empty.
    prefix with hashmap pattern perhaps..
    decision:
        nums = [1,-1,3,-1,1] what are my actions with prefix array.
        hashmap = {0:1}, base case where 0 denote
        prefix sum from i to j is equal to prefix[j] - prefix[i-1], we shall use 1-index prefix to simplify
        a subarray is valid if its k == prefix[j] - prefix[i-1]
         so we can just convert this to prefix[i-1] == prefix[j] - k 
         and store prefix[i-1] in the hashmap and see if we if the requiredPrefix i.e. prefix[j]-k matches in the future and add that to the running count 
       
    space optimisation,
    since we are saving previous prefix sums in hashmap, we really don't need anything more than the current one so it can just be changed to curr_prefix as a single int variable instead of array
"""
# @leet start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_prefix = 0
        frequencyOfPrefix = {
            0:1
        }
        count = 0
        for num in nums:
            curr_prefix += num
            requiredPrefix = curr_prefix - k
            count += frequencyOfPrefix.get(requiredPrefix,0)
            frequencyOfPrefix[curr_prefix] = frequencyOfPrefix.get(curr_prefix,0)+1 
        return count

            
       
        
            
# @leet end
