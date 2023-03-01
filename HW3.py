#!/usr/bin/env python
# coding: utf-8

# # HW 3
# 
# **Upload two files** to Gradescope: 
# * `HW3.py` (which will be autograded)
# * `HW3.ipynb` (run all cells to make sure that outputs are visible)
# 
# ___

# In[1]:


import math
import random
import numpy as np
import matplotlib.pyplot as plt
import time


# ### Function Threshold
# 
# Suppose `func(n)` is a monotonically increasing function. Write a function **`exceed_func3(func, thresh, start, end)`** that **uses binary search** to find the largest `n` between positive integers `start` and `end`, inclusive, such that `func(n)` is less than or equal to a given threshold. If there is no such `n`, return `None`.

# In[2]:


def exceed_func3(func, thresh, start, end):
    if func(start) > thresh:
        return None
    elif func(end) < thresh:
        return end
    else:
        mid = math.floor((start + end)/2)
        if func(mid) == thresh:
            return mid
        elif func(mid) > thresh:
            return exceed_func3(func, thresh, start, mid - 1)
        else:
            return exceed_func3(func, thresh, mid + 1, end)


# ### Max SubList Problem
# Given a list of numbers, find a contiguous sublist with the largest sum. If there is more than one sublist with the same max sum, return any of them. Assume that the list contains both positive and negative numbers.
# 
# * Write a function **`max_sublist1(nums, start, end)`** that implements the brute-force (exhaustive search) solution, examining every possible sublist. It returns a 3-element tuple containing the indices that correspond to the first and last elements of the max sublist (inclusive), and the max sum.
# 
#   Example:<br>
#   `max_sublist1([1, -4, 13, -5, 7], 0, 4)` returns `(2, 4, 15)` which corresponds to the max sum of $13-5+7 = 15$ and the starting and ending indices of $2$ and $4$.
# 
# * Write a function **`max_sublist2(nums, start, end)`** that implements the divide-and-conquer solution. Recall that this is a $\Theta(n \log n)$ algorithm.
# 
# * Find a linear time algorithm for the max sublist problem. Write a function **`max_sublist3(nums, start, end)`** that implements this $\Theta(n)$ algorithm. (*Hint:* Given a starting index, as long as the accumulated sum is positive, keep adding elements. If the sum becomes negative, reset the starting index.)

# In[3]:


def max_sublist1(nums, start, end):
    S = 0
    for i in range(len(nums)):
        for j in range(i + 1,end + 1):
            if sum(nums[i:j + 1]) > S:
                S = sum(nums[i:j + 1])
                ind1 = i
                ind2 = j
    if nums[0] > S:
        S = nums[0]
        ind1 = 0
        ind2 = 0
    elif nums[-1] > S:
        S = nums[-1]
        ind1 = len(nums) - 1
        ind2 = len(nums) - 1
    return (ind1,ind2,S)


# In[4]:


max_sublist1([1, -4, 13, -5, 7], 0, 4)


# In[21]:


def max_sublist2(nums, start, end):
    if start == end:
        return (start,start,nums[start])
    elif end - start == 1:
        if nums[start] > nums[end]:
            return (start,start,nums[start])
        elif nums[start] < nums[end]:
            return (end,end,nums[end])
        else:
            return(start,end,2*nums[start])
    else:
        mid = math.floor((start + end)/2)
        sum1 = 0
        rightsum = 0
        e2_1 = 0
        for i in range(mid,end + 1):
            sum1 += nums[i]
            if sum1 > rightsum:
                rightsum = sum1
                e2_1 = i
        sum2 = 0
        leftsum = 0
        s2_1 = 0
        for i in range(mid,start - 1,-1):
            sum2 += nums[i]
            if sum2 > leftsum:
                leftsum = sum2
                s2_1 = i
        if (mid - 1 - start) == 1 or (mid - 1 - start) == 0:
            s1, e1, res1 = max_sublist2(nums, start, mid - 1)
        else:
            s1, e1, res1 = max_sublist2(nums, start, mid - 1)
        if (end - mid - 1) == 1 or (end - mid - 1) == 0:
            s2, e2, res2 = max_sublist2(nums, mid + 1, end)
        else:
            s2, e2, res2 = max_sublist2(nums, mid + 1, end)
        res3 = max(rightsum + leftsum - nums[mid],rightsum,leftsum)
        res4 = max(res1,res2,res3)
        if res4 == res1:
            return (s1,e1,res4)
        elif res4 == res2:
            return (s2,e2,res4)
        else:
            if res4 == nums[mid]:
                return (mid,mid,res4)
            elif res4 == rightsum:
                return (mid,end,res4)
            elif res4 == leftsum:
                return (start,mid,res4)
            elif res4 == sum(nums):
                return (start,end,res4)
            else:
                return (s2_1,e2_1,res4)


# In[6]:


max_sublist2([1, -4, 13, -5, 7], 0, 4)


# In[22]:


max_sublist2([1, -4, 13, -5, 7, -22, 44], 0, 6)


# In[7]:


def max_sublist3(nums, start, end):
    max1 = nums[0]
    max2 = 0
    s = start
    slst = [s]
    e = end
    for i in range(len(nums)):
        max2 = max2 + nums[i]
        if max2 < 0:
            max2 = 0
            slst.append(i + 1)
        elif (max1 < max2):
            max1 = max2
            e = i
            s = slst[-1]
    if max1 == nums[-1]:
        s = len(nums) - 1
        e = len(nums) - 1
    return (s,e,max1)


# In[8]:


max_sublist3([1, -4, 13, -5, 7], 0, 4)


# **Compare the runtimes for the 3 versions.**

# In[9]:


def exec_time():
    return time.time()


# In[10]:


lst1 = []
for i in range(1000):
    lst1.append(i)
#start1 = exec_time()
m1 = max_sublist1(lst1, 0, lst1[-1])
#end1 = exec_time()
#end1 - start1


# In[15]:


lst2 = []
for i in range(10000):
    lst2.append(i)
#start2 = exec_time()
m2 = max_sublist2(lst2, 0, lst2[-1])
#end2 = exec_time()
#end2 - start2


# In[12]:


lst3 = []
for i in range(10000):
    lst3.append(i)
#start3 = exec_time()
m3 = max_sublist3(lst3, 0, lst3[-1])
#end3 = exec_time()
#end3 - start3

