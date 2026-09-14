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
We need to return the length of the longest possible substring/subbaray i.e. a contigious series of element from the given string,
that satisfies the following condition.
    It needs to be the same element, ie. AA is valid, AB is not.
    We can do k character replacements in order to extend this longest subbaray

constraints, s.length : [1,10e5]. A O(n^2) solution would be invalid. We need to find something faster.
S only has uppercase english letter.
k: [0,s.length]

Direction: 
    we could use a simple sliding window as increasing the size of the sliding window will either increase or keep same the length of the current longest array.
        similarly, shrinking it will decrease it or keep it the same.
        as such, monotonicity for sliding window is satisifed.
    Also, we can keep a frequency map for keeping the frequencies of the current subwindow in mind,
        When we add a new element, we change the current-most-frequent element based on the max(freq[current-most-frequent],freq[new_element]) after updating the freq of the new element.
        then we store this in a global maximum after comparing with it.
        
    albiet this is still only considering simple longest character subbaray. To consider the character replacements...

    

    we could add the condition as,
        expand towards the right uncondtionally with a for loop 
        in each for loop, when a new maximally frequent char is found, we can use subtract the count of it to the count of the size of the subarray and shrink it if the difference is greater then k.

    we could also use a array of size 26 to act as the frequency map as we only have uppercase english letters to consider..

dry run:
ABAB

"""


# @leet start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freqMap = [0]*26
        left= 0
        maxFreq = 0
        maxSeq = 1
        for right in range(len(s)):
            curr_char = s[right]
            freqIdx = ord(curr_char) - ord('A')
            freqMap[freqIdx] +=1
            maxFreq = max(maxFreq,freqMap[freqIdx])
            while (right - left + 1 - maxFreq) >k:
                freqMap[ord(s[left])-ord('A')]-=1
                left += 1
            maxSeq = max(maxSeq,right-left+1)

        return maxSeq

        
# @leet end
