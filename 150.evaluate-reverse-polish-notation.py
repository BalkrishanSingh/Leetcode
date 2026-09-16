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
We need to evaluate a list of strings where the list represents a reverse polish notation expression and we need to return the result

    the logic of reverse polish notation can be reperesented cleanly by a stack,
    we add operands to a stack as we stack the array.
        then when we encounter any operator, we pop last two operands, compute and add the value to stack.
    This is repeated until all values are processed.

    We could use a simply if else chain to check for each operand 

"""
# @leet start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evalStack = []
        for token in tokens:
            if token in {"+","*","/","-"}:
                secondOperand = evalStack.pop()
                firstOperand = evalStack.pop()
                if token == "+":
                    evalStack.append(firstOperand+secondOperand)
                elif token == "*":
                    evalStack.append(firstOperand*secondOperand)
                elif token == "/":    
                    evalStack.append(math.trunc(firstOperand/secondOperand))
                elif token == "-":
                    evalStack.append(firstOperand-secondOperand)
            else:
                evalStack.append(int(token))
        return evalStack.pop()
        
# @leet end
