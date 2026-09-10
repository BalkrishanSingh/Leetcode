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
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Since it's a key value data structure, we probably want to use a hashmap in the end.. 
But we do have multiple values for the same key so we probably want to use a linear datastrucute there?

We have 10e7 possible timestamp values for a given single key and we definitely need to use Log(n) time complexity to be able to compute this in a usuable time.

I'm considering we could use a dictionary with {string:list[tuple(int,string)]} where we can use binary search on the first element of the tuple,

the binary search will focus on the given target timestamp and aim to find the tuple pair just equal or under it..

Lets see how will the structure of the binary search ehre look like..

We initiate with the size of the list of the keymap resolution -1 as right and left is 0.
we also keep a value called curr which we can track to see what is a value under the given time stamp.
then we run a while loop with left <= right:
    conditions should be to update simple mid to right 





Implement the TimeMap class:

	* TimeMap() Initializes the object of the data structure.
	
	* void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
	
	* String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

    TimeMap timeMap = new TimeMap();
	│ timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
	│ timeMap.get("foo", 1);         // return "bar"
	│ timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
	│ timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
	│ timeMap.get("foo", 4);         // return "bar2"
	│ timeMap.get("foo", 5);         // return "bar2"

    
     key and value consist of lowercase English letters and digits.


     1 <= key.length, value.length <= 100

     1 <= timestamp <= 10^7
        
     2 * 10^5 

"""

# @leet start
class TimeMap:

    def __init__(self):
        self.tempHash = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.tempHash:
            self.tempHash[key].append((timestamp,value))
        else:
            self.tempHash[key] = [(timestamp,value),]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.tempHash:
            values = self.tempHash[key]
            curr = None
            left = 0
            right = len(values)-1
            while left<= right:
                mid = left+(right-left)//2
                if values[mid][0] <= timestamp:
                    curr = mid
                    left = mid + 1
                else:
                    right = mid-1 
            if curr != None:
                return values[curr][1]
            
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @leet end
