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
    def longestCommonPrefix(self, strs: list[str]) -> str:
        max_prefix = strs[0]
        for i in strs[1:]:
            if max_prefix == "":
                break
            while max_prefix != "":
                if i.startswith(max_prefix):
                    break
                else:
                    max_prefix = max_prefix[:-1]
        return max_prefix
# @leet end
