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
given a string, we need to find out if it's a palindrome, keeping in mind the constraints that we need to ignore case, and remove non alphanumeric characters.

Since it's a check for a palindrome, we can simply use a stack, if something matches the top or is the middle element, we pop, if it doesn't then if its alphanumeric we add it to stack.
if stack empty we return true.

For doing alphanumeric checks in python, we can use. str.isalpha() i believe and use islower to convert it down.

"""
# @leet start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsedStr = ""

        for chr in s:
            if chr.isalnum():
                parsedStr += chr    
        parsedStr = parsedStr.lower() 
        return parsedStr[::] == parsedStr[::-1] 
   

        
# @leet end
