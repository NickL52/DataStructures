#!/usr/bin/env python
# coding: utf-8

# # Lab1
# At the end of class **upload two files** to Gradescope: 
# * `Lab1.py` (which will be autograded)
# * `Lab1.ipynb` (run all cells to make sure that outputs are visible, especially plots)
# 
# **All Lab solutions will be graded** for correctness and completion. If you do not finish a Lab during class, upload your partial work. Then you will have a week to submit your completed solutions to Gradescope.
# 
# ___

# In[1]:


import random
import numpy as np
import matplotlib.pyplot as plt
import time


# # Truchet Tiles
# A *Truchet tile* is a square tile that is colored on one side of a diagonal. 
# 
# <img src="http://www.coloradomath.org/python/truchet.jpg" width="262" height="64" />
# 
# The function below displays a single borderless Truchet tile at a given position $(x,y)$ with corner at LL or LR (UR and UL cases omitted). 
# * Does the code work for `tile((2, 3), 'LL')`?
# * Can the code be written for all 4 corner cases without a large `if` statement?

# In[2]:


def tile(loc, corner):
    xpos, ypos = loc
    dic = {'LL':[[0,1,0], [0,0,1]], 'LR':[[1,1,0], [0,1,0]], 'UL':[[0,1,0], [1,1,0]], 'UR':[[0,1,1], [1,1,0]]}
    xvals = xpos + np.array(dic[corner][0])
    yvals = ypos + np.array(dic[corner][1])
    plt.fill(xvals, yvals)
    plt.axis('equal')
    plt.axis('off')


# In[3]:


tile((2, 3), 'LL')


# Write an improved version of **`tile(loc, corner)`** that works for all 4 corner cases. Set the aspect ratio to be equal and remove the plot frame.

# In[4]:


def cum_sum1(nums):
    '''Return the cumulative sum of a list of numbers'''
    return [sum(nums[:i]) for i in range(1, len(nums)+1)]


# In[5]:


def cum_sum2(nums):
    S = 0
    lst = []
    for i in range(len(nums)):
        S = S + nums[i]
        lst.append(S)
    return lst


# In[10]:


time1 = []
time2 = []
for i in [3,30,300,3000,30000]:
    x = [random.random() for j in range(i)]
    start1 = time.time()
    cum_sum1(x)
    end1 = time.time()
    t1 = end1 - start1
    time1.append(t1)
    start2 = time.time()
    cum_sum2(x)
    end2 = time.time()
    t2 = end2 - start2
    time2.append(t2)
print(f'{"n      cum_sum1 time      cum_sum2 time"}')
print(f'{"3      "}{time1[0]:.11f}{"      "}{time2[0]:.11f}')
print(f'{"30     "}{time1[1]:.11f}{"      "}{time2[1]:.11f}')
print(f'{"300    "}{time1[2]:.11f}{"      "}{time2[2]:.11f}')
print(f'{"3000   "}{time1[3]:.11f}{"      "}{time2[3]:.11f}')
print(f'{"30000  "}{time1[4]:.11f}{"      "}{time2[4]:.11f}')


# ### Comparing Cumulative Sum Runtimes
# **Write code** to display a table comparing the execution times (in seconds) for `cum_sum1()` and `cum_sum2()`. First create a list of 30000 `random.random()` numbers. Then pass the first $n$ list elements to the two functions for $n=3, 30, 300, 3000, 30000$. **Use f-strings.**
# 
# Here is a sample table. Runtimes will vary depending on your code for `cum_sum2` and the computer you are using. For large `n`, your code should run at least 10 times faster than the inefficient version. It is not necessary to exactly match the format of this table.
# ```
#    n    cum_sum1   cum_sum2
#           time       time
# ---------------------------
#     3   0.000026   0.000009
#    30   0.000017   0.000004
#   300   0.000540   0.000033
#  3000   0.036902   0.000246
# 30000   2.718307   0.001947
# ```

# ___
# 
# # Extra Problems
# This problem will not be graded.

# Truchet tiles can form intricate patterns.
# 
# <img src="http://www.coloradomath.org/python/truchet_tiling_color.jpg" width="419" height="278" />
# 
# Create a function that will display a Truchet tiling given the number of grid rows and columns. Possible options:
# * The colors can be specified or the default pyplot colors can be used.
# * The corners can be specified or chosen randomly.

# In[ ]:




