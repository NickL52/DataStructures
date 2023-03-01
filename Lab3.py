#!/usr/bin/env python
# coding: utf-8

# # Lab3

# In[1]:


import random
import numpy as np
import time


# ### Jupyter Debugger
# https://jupyterlab.readthedocs.io/en/stable/user/debugger.html
# 
# Practice debugging the following code by setting breakpoints and examining the values of the variables.

# In[2]:


# helper function to demonstrate the debugger step function
def fetch_bin(n):
    return bin(n)[2:]


# In[3]:


def fast_power(b, n):
    '''Calculate b**n using squares of powers where n is a non-negative integer.'''
    result = 1
    b_exp = b
    n_bin = fetch_bin(n)
    
    for bit in reversed(n_bin):
        if bit == '1':
            result *= b_exp
        b_exp **= 2
    
    return result


# In[4]:


fast_power(3, 13)


# ### Code Tracing and Complexity
# Each of the following 4 functions uses a loop to compute a value. For each function:
# * Explain what the function is computing.
# * Use an asymptotic expression to estimate the number of operations performed within the loop (not counting the operations of the loop itself). 
# 
# Choose from the following possible answers. Justification is not necessary.<br>
# 1. $\Theta(1)$
# 2. $\Theta(\log n)$
# 3. $\Theta(\log (m+n))$
# 4. $\Theta(\log (mn))$
# 5. $\Theta(n)$
# 7. $\Theta(m+n)$
# 8. $\Theta(mn)$
# 6. $\Theta(n\log n)$
# 9. $\Theta(mn\log(mn))$
# 10. $\Theta(n^2)$
# 11. $\Theta(m^2n^2)$
# 12. $\Theta(n^2\log n)$
# 12. $\Theta(m^2n^2\log (mn))$
# 13. None of these

# ### Example 1
# * Explain what FUNC1 is computing.
# * Find an asymptotic expression for the number of multiplications performed.
# ```
# FUNC1(m, n)
#     x = 0
#     for i = 1 to m
#         for j = 1 to n
#             x = x + i*j
#             
#     return x
# ```

# **Explain what FUNC1 is computing:**
# 
# 

# FUNC1 computes the following sum: 1 + 2 + 3 + ... + n + 2 + 4 + 6 + ... + 2n + 3 + 6 + 9 + ... + 3n + ... + m + 2m + 3m + ... + nm

# In other words, it computes the following: $\sum \limits _{i=1} ^{m} \sum \limits _{j=1} ^{n} {i}{j}$

# In[10]:


asymp_func1_mults = 7


# ### Example 2
# * Explain what FUNC2 is computing.
# * Find an asymptotic expression for the number of additions performed.
# ```
# FUNC2(m, n)
#     x = 0
#     for i = 1 to m
#         for j = i to n
#             x = x + i + j
#             
#     return x
# ```

# **Explain what FUNC2 is computing:**
# 

# FUNC2 computes the following sum: 2 + 3 + 4 + ... + n + 1 + 4 + 5 + 6 + ... + n + 2 + 6 + 7 + 8 + ... + n + 3 + ... + 2m + 2m + 1 + 2m + 2 + ... + 2m + n

# In other words, it computes the following: $\sum \limits _{i=1} ^{m} \sum \limits _{j=i} ^{n} i + j$

# In[102]:


asymp_func2_adds = 7


# ### Example 3
# * Explain what FUNC3 is computing.
# * Find an asymptotic expression for the number of multiplications performed.
# * Find an asymptotic expression for the number of `max` comparisons performed.
# ```
# FUNC3(A)
#     m = 0
#     for i = 1 to A.length
#         for j = i+1 to A.length
#             m = max(A[i]*A[j], m)
#             
#     return m
# ```

# **Explain what FUNC3 is computing:**
# 

# FUNC3 finds the highest value created by multiplying two elements of a list

# In[46]:


asymp_func3_compares = 10


# ### Example 4
# * Explain what FUNC4 is computing.
# * Find an asymptotic expression for the number of multiplications performed.
# * Find an asymptotic expression for the number of additions performed.
# ```
# FUNC4(n)
#     i = 1
#     x = 0
#     while i <= n
#         x = x + i
#         i = 2*i
#             
#     return x
# ```

# **Explain what FUNC4 is computing:**
# 

# I'm not sure how to explain what FUNC4 does without just describing the code above.

# In[81]:


asymp_func4_adds = 2


# ___
# 
# # Extra Problems
# The following problem is optional.

# ### Compare Runtimes for Squaring Numbers
# When squaring each number `x` in a list, is it faster to execute `x*x` or `x**2`? What if we use numpy vectorization? Write four different functions that will take a list (or array) of numbers and return a list (or array) of the squares.
# * **`square_nums1(num_list)`**: Takes a list of numbers and uses multiplication: `x * x` and a list comprehension to square the numbers.
# * **`square_nums2(num_list)`**: Takes a list of numbers and uses exponentiation: `x ** 2` and a list comprehension to square the numbers.
# * **`square_nums3(num_array)`**: Takes an array of numbers and multiplies the array by itself using `*` vectorization. It returns the result as an array.
# * **`square_nums4(num_array)`**: Takes an array of numbers and squares the array using `**2` vectorization. It returns the result as an array.
#     
# Compare the runtimes for these 4 functions using a list of 50000 random numbers as input.

# In[ ]:




