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
#
"""Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

	* MinStack() initializes the stack object.
	For initialization, we need 

	* void push(int value) pushes the element value onto the stack.
	
	* void pop() removes the element on the top of the stack.
	
	* int top() gets the top element of the stack.
	
	* int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Summary:
    we need to create a class that has constant time operations to push, pop and findMin value of a stack.

    I think, we maintain two arrays.
        where, stack represents the basic stack.
        and minimumsSoFar represent the minimum value so far.
        
        If a ith element is added, then we compare with i-1 element in the minimumsSoFar and decide on the new minimum with min.
        if ith element is popped, we remove the ith element of minimumsSoFar as well.
        th



"""



# @leet start
class MinStack:

    def __init__(self):
        self.stack = [] 
        self.minimumsSoFar = []

    def push(self, value: int) -> None:

        self.stack.append(value)
        if len(self.minimumsSoFar) > 0:
            self.minimumsSoFar.append(min(self.minimumsSoFar[-1],value))
        else:
            self.minimumsSoFar.append(value)


        
        

    def pop(self) -> None:
        self.minimumsSoFar.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimumsSoFar[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @leet end
