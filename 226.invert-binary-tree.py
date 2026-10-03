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
Given problem asks us to invert a tree and return the root of that tree where inversion refers to swapping the inverted left subtree of a node with the inverted right subtree of a node if either of them exists.

it can be solved quite simply with recursion.

"""
# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return 
        if not root.left and not root.right:
            return root
        root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root
# @leet end
