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
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
    given n cars where n is bounded by [1,10e5], we need to find something faster than O(n^2) for our solution
    given target position where cars reach.

You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the i^th car and speed[i] is the speed of the i^th car in miles per hour.
    each char is described by two things, positon and speed.
        position i is the starting position of the ith car
        speed i is the current speed of the ith car.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
        No overtaking allowed, i.e. A set of different cars that began at different speeds and location will follow the same speed to the destination after merging into a fleet.

A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.
        

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
    Edge case where a car just meets up at the end.

Return the number of car fleets that will arrive at the destination.
        
for two given arrays of position and speed of cars, 
    we need to find how many sets of car arrive at the desitnation 
        where cars merge into a single set based on the location
            cars at the same location are in the same set 
                a set follows the speed of the car with the minimum speed in the group.

We need to first sort in the reverse order the given array by position so that a further car doesn't form a fleet with one that is present earlier and is processed earlier.
In addition, we use a tuple to keep position and speed of a car linked.

While working through the cars, we need to consider the time remaining which is (target-position)/speed.
we can use a stack to store car fleets, if a 
    
"""
# @leet start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedCars = sorted(zip(position,speed),key=lambda x: x[0],reverse=True)
        monotonicStack =[]
        for p,s in sortedCars:
            monotonicStack.append((target-p)/s)
            if len(monotonicStack)>=2 and monotonicStack[-1] <= monotonicStack[-2]:
                monotonicStack.pop()
        return len(monotonicStack)


        
# @leet end
