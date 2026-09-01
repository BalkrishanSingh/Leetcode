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
    def romanToInt(self, s: str) -> int:
        sum = 0
        roman_values:dict = {
            "I"     :      1, 
            "V"     :      5,
            "X"     :      10,
            "L"     :      50,
            "C"     :      100,
            "D"     :      500,
            "M"     :      1000
        }
        for i,literal in enumerate(s[:len(s)-1]):
            if roman_values[literal] < roman_values[s[i+1]]:
                sum -= roman_values[literal]
            else:
                sum += roman_values[literal]
                
        return sum + roman_values[s[-1]]
# @leet end
