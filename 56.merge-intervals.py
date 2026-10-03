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
Given problem asks us to return a array of non overlapping intervals, given a array of arrays where each array at each index denotes [start_interval, end_interval] of that interval i.

Constraint, the number constraints can be upto 10e4 and are at minimum 1.

Solution:
    a simple solution would be to iterate over the given intervals,
        then we compare the last interval in the results array and see if it should be merged based the following rule:
            given, a,b starting and ending interval of results[-]1
            and c,d start and end interval of intervals[i].
            if the maximum of the starting times is smaller or equal then the minimum of the end times,
                 then there is overlap.
                 result[-1] = min(a,c), max(b,d) 
                 
            we should ideally sort the intervals array first for this soolution to work.

"""
# @leet start
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        sorted_intervals = sorted(intervals,key=lambda x : x[0])
        results = []
        for i in range(len(sorted_intervals)):
            if not results:
                results.append(sorted_intervals[i])
                continue 
            a,b = results[-1]
            c,d = sorted_intervals[i]
            if max(a,c) <= min(b,d):
                results[-1] = [min(a,c),max(b,d)]
            else:
                results.append(sorted_intervals[i])
        return results

        
# @leet end
