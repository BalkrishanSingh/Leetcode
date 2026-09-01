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

# @leet start
class Solution:
    def isValid(self, s: str) -> bool:
        stack:list[str] = []
        match:dict[str,str] = {
            ')': '(', '}': '{', ']':'['
        }
        i:int = 0
        while i < (len(s)):
            if s[i] in match.values():
                stack.append(s[i])
            else:
                if stack and stack[-1] == match[s[i]]:
                    stack.pop()
                else:
                    return False
            i +=1 

        return not stack
# @leet end
