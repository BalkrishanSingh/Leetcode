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
summary: 
For a given array of size n and sliding window size k,
we need to return a list of the maximum number in each position of the sliding window 
as it slides over 1 index at a time from left to right.

A simple brute force solution would be to iterate over the arrray from [0,n-k-1] where at each step, we append max(arr[i:i+k]) to the result.
this would be a O(N^2) solution.

The given constraints however require a Log(n) or O(n) solution..

Optimally, the solution seems to be a monotonic deque 
where the left most index will always contain the current maximal value and return it each time.

we loop overall elements in the array from [0,n-1] and we find the start of the sliding window with i-k-1 
We only need to check at the start of the loop if this value is invalid or not and thereby remove it if so.
We store only indexes in the deque and as such we can compare by checking if deque[0] < i-(k-1).
Next we need to setup the logic for maintaining the monotonicity of the deque.
    For the current element 
    at each step, we check if DQ itself exists or not
    then we check if the left most value is greater than the current element. If yes, end loop
    else we pop it and loop over
    then we add the current element to the right of the deque
    
then we append the left most element to the solutions array. 

We do have a slight logical issue here where we will get N values added to the results array and not N-K-1.

which is a slight issue...
I think it would be optimal to wait for i to be >= k-1 to add to the results array perhaps?

for example.. 
[1,3,-1,-3,5,3] with k =3.
dq res i i-k-1
0 [] 0  -2
1 [] 1  -1
1 [3] 2  -0
1 [3,3] 3 1, popped.
4 [3,3,5]4 2
3 1 1 3 , 3

""
# @leet start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        dq = deque()

        for i in range(len(nums)):
            while dq and dq[0]< i -(k-1):
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if dq and i >= k-1:
                results.append(nums[dq[0]])
        return results
        
# @leet end
