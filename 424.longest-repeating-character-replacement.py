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
for a given string s, we need to find the longest subarray that has the same letter, given that we can perform k replacement of characters.

If we just iterate over the entire array with a variable sliding window that increases from the right constantly,
and shrinks from the left whenever it meets condition:
    while the difference of the length of the subarray and the frequency of the most common element is greater than k.

given constraints also suggest we use a O(n) or O(nlogn) solution which would be satisfied by sliding window.


"""


# @leet start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 1 
        left = 0
        chrFrequency = [0]*26
        highestFreq = -1
        for right in range(len(s)):
            idx = ord(s[right]) - ord("A")
            chrFrequency[idx] +=1
            highestFreq = max(highestFreq,chrFrequency[idx])
            while (right-left+1)- highestFreq > k:
                chrFrequency[ord(s[left])-ord("A")] -=1 
                left +=1 
            maxLen = max(maxLen,right - left + 1)
        return maxLen
            
        
# @leet end
