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
given position and speed of N cars, we need to find groups of car that will reach a given target position with the condition that no car can overtake another.

we need to first sort the cars on the basis of position to allow further cars to not be stopped by earlier cars.

Secondly, We need to use time as a metric instead of both positon and speed to compare cars,
    i.e. we use (target-iPosition)/iSpeed to find the iTime required for a car i to reach target.

How do we find the number of car fleets..


given constraints suggest that our target value is [0,10e6], speed [0,10e6] as well and n is [1,10e5]. We can't go slower then nlogn in time complexity.
All positions given are unique so we will not have two different cars with different speeds but at same position, ie something that should be in a group from the getgo.


Dry Run:
    input,
     target = 12,
     positons and speed after sorting? 
        0,1
        3,3
        5,1
        8,4
        10,2
    I think we should begin from the back of the sorted array so as to not entangle later cars with earlier cars unnessarily
        
        i = 4,
            10,2 
            time = 12-10/2 = 1
        i = 3,
            8,4
            12-8/4 = 1
        i = 2
            5,1
            12-5/1 = 7
        i = 1 
            3,3
            12-3/3 = 3
        i = 0
            0,1
            12/1 = 12
        (10,8), (0) and (3,5) forms a group according to example.
        I can see that the main condition seems to be that the newer value should be less than or equal to the previous value.
            which seems to make sense as it represents the time for a given car to reach target,
                if a earlier car requires less time than a later car then the earlier car will be restricted by the later car.
            however, if the later car requires more time i.e. it is slower, it doesn't matter and forms a separate group.
    we can use simple array,
        where we insert time into the array if its greater then the last one to represent another independent fleet.
            
    I do doubt if we need to update the last time in the array when it does form a new car fleet 

    
"""
# @leet start
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        results = []
        cars = sorted(zip(position,speed),key=lambda x:x[0],reverse=True)
        for iPosition,iSpeed in cars:
            time = (target-iPosition)/iSpeed
            if not results or  time > results[-1]:
                results.append(time)
        return len(results)



        
# @leet end
