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
'''
For this question, we are asked to find all the triplets of a given array that add up to 0,
we need to avoid duplicate triplets based on values and we can't use the same value more than once in the triplet, so the minimum viable input needs to be 3 in length.

i.e nums[i] + nums[j] + nums[k] == 0 where i!=j,i != k, and j != k,
    we can treat this as, nums[i] + nums[j] = -nums[k]

to avoid duplicates in triplets, we use a hashmap to store tuples of sorted tuples.

to find the tuples themselves,
    we can use a sorted array with two pointers in the inner loop to find if values add upto a target value k which is iterating over the entire list in the outer loop.

a simple solution would have been to use a triple nested loop where we run that simple check each time.

'''

0+1 >


# @leet start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums = sorted(nums)
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            left = k+1
            right = len(nums)-1

            while left < right:
                sum =  nums[left]+nums[right] 
                if sum == -nums[k]:
                    triplet = nums[k],nums[left],nums[right]
                    triplets.append(triplet)
                    while left < right and nums[left] == nums[left+1]:
                        left+=1 
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left +=1 
                    right-=1


                elif sum < -nums[k]:
                    left +=1  
                else:
                    right -=1 

        return triplets        
# @leet end
