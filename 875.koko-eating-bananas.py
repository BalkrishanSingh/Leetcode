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
Koko loves to eat bananas. There are n piles of bananas, the i^th pile has piles[i] bananas. The guards have gone and will come back in h hours.
    
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile.

If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

For a given array of values,
    we need to find a minimum value k 
        that will allow us to make every value in that array to 0 by subtracting in atmost h loops.
            this will form the validation function for binary search,
                
                The function will follow the logic. (k)
                    index = 0
                    step = 0
                    while step <h and index < len(piles):
                        steps += max(math.ceil(piles[index]/k),1)
                        index +=1
                    this should be of order n
                        

            the range of the values reasonable for k is [0,max(piles)] while the constraints themselves are [1,10e9].
        We need to use binary search on the answer to navigate this large search space.
        At each step, we validate the mid value with a checking function.
    

Constraints:

	* 1 <= piles.length <= 10^4
	
* piles.length <= h <= 10^9
	
	* 1 <= piles[i] <= 10^9



"""
# @leet start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkValidity(k:int)-> int:
            if k == 0:
                return False
            
            currTime = 0
            for pile in piles:
                currTime += (pile + k - 1) // k
        
                if currTime > h:
                    return False
            return True
        left = 0
        right = max(piles)
        ans = right
        while left <= right:
            mid = (left+right)//2
            if checkValidity(mid):
                ans = mid
                right = mid -1
            else:
                left = mid+1 
        return ans
        
# @leet end
