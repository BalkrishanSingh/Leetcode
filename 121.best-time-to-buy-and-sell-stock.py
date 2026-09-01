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
    def maxProfit(self, prices: List[int]) -> int:  
        current_max_profit:int = 0
        current_cheapest: int = prices[0]
        for i in range(1, len(prices)):
            predicted_profit:int = prices[i]- current_cheapest
            if current_max_profit < predicted_profit:
                current_max_profit = predicted_profit   
            if current_cheapest > prices[i]:
                current_cheapest = prices[i]
             
        return current_max_profit
# @leet end
