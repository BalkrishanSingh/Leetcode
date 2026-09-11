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
Summary:
    we need to find the sum of water that is at possible to be collected at each index in a given array of heights,
    main restriction on the water that is possible at a index is the height of the indexes surrounding it 
    and the height of the index itself.

    For example, for given input, 4,2,0,3,2,5. We can only store 1 unit of water at index 4 because the minimum of the left and right highest heights is 3 and the value of the height at that index itself is 2.

    Since we need to consider the left and right max of each point, we can use a prefix and suffix array where each index contains the highest height so far from either direction of index i and then we can use the formula water[i] = max(min(left_max[i],right_max[i])-height[i]),0)
    this prefix and suffix solution could be made more optimal as we'd need 3 loops of size n and O(n) space to find the solution. 
    constraints are, n:[1,2*10e4] which is large and as such require a nlogn or n time complexity solution ideally..

    Aside from the prefix suffix solution, for a simple brute force solution, we can loop over the entire array
    then loop over twice more where one loop is from 0 to i and another is i to n-1 to find the left largest and right largest for each element for a O(n^3) solution..

    A more optimal solution could be to simply use two pointers left and right. 
    We only update the value of water at a index or store it in a sum if we are about to move past that node with the lexft or right index and as there should be no possible way it has a higher left_max or right_max, based on what we incremented or decremented.
    to find the water at that node, we should use the stored left_max and right_max found so far

    implementing solution.



"""
# @leet start
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1 
        left_max = height[left]
        right_max = height[right]
        water = 0 
        while left < right:
            if left_max < right_max:
                left +=1 
                left_max = max(left_max,height[left])
                water += max(left_max - height[left],0)
            else:
                right -= 1
                right_max = max(right_max,height[right])
                water += max(right_max - height[right],0)
        return water



        
# @leet end
