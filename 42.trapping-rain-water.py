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
    Given a list of heights for a given area, we are asked to find the sum of water level at each position in that array given that water accumulates to the the minimum of the heighest height on left and right of the index.
    
    For a given index i, water at i is given by (min(leftmax,rightmax)-height[i],0)
    we should only try to calculate this value if we are sure that the value min(leftmax,rightmax) can't increase any further.
    to find the next best height, we increment the smaller max currently towards the direction of the higher max as the bottleneck is the smaller value.
    and if we move past a index, then that index will never be having a higher value so we calculate the water level

    we can simply use a two pointer approach to decide this
    where left pointer starts at 0,
    right at n-1
    we keep a left max and right max going and initially set it to the values themselves.
    then we just keep running the formula and increment left or right.
    each time calculating water by using the height[left] or height[right] based on what is incremented.

    we should calculate water level at a step before incrementing ofcourse as that is a common error i remember in two pointer approach
    
    We should use left <= right for the terminating conditon as we are using len(right)-1 as our index and we only save the water value before we increment so, so we need the next iteration.

    203
    left = 0
    right = 2
    0
    left = 1 
    right = 2
    2
   

"""
# @leet start
class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1 
        leftmax = height[0]
        rightmax = height[right]
        sum = 0
        
        while left <= right:
            if leftmax < rightmax:
                sum += max(leftmax -height[left],0)
                leftmax = max(leftmax,height[left])
                left +=1
            else:
                sum += max(rightmax - height[right],0)
                rightmax =max(rightmax,height[right])
                right-=1
        return sum

                

        
# @leet end
