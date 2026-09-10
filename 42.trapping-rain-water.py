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
we are given a array height of size n,
each height[i] represents the given height of the elevation at that point?
we need to find how much water the entire area can trap.

for example, [0,1,0,2], it should trap 1 unit of water between index 1,3.

No water is trapped on 0 as there is no left wall.

or for [2,1,2,1], another unit of water is trapped between index 1,0,1. No water on index 3 as no right wall.

So as a base case, we can exclude the water on the 0 and n-1 indexes.

we need to loop over the entire array at a minimum because to find the maximum water trapped,
we need to check the height at each index
as water at a index seems to be the min(min(tallest_left_wall,tallest_right_wall) - height[i],0)
the min basecase is because the we can't have negative water on a peak.

Direction:
    we can't just traverse in a single direction,

constraints:
    n: 2*10^4. I believe a n^2 solutin should work.
       

what exactly is my logic here that is going wrong?



"""
# @leet start

class Solution:
    def trap(self, height: List[int]) -> int:
        left_highest= [0]*(len(height)+1)
        right_highest =[0]*(len(height)+1)
        water = 0
        #populating left_highest
        left_highest[0] = height[0]
        for i in range(1,len(height)-1):
            left_highest[i] = max(left_highest[i-1],height[i])
        right_highest[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            right_highest[i] = max(right_highest[i+1],height[i])
        for i in range(1,len(height)-1):
            water += max(min(left_highest[i-1],right_highest[i+1])-height[i],0)
        return water

                    
# @leet end
