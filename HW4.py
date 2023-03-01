#!/usr/bin/env python
# coding: utf-8

# # HW 4
# ___

# In[1]:


import numpy as np


# ### Polynomials
# A polynomial $P(x)$ can be represented by an array of coefficients in *increasing* degree order. Examples are shown in this table:
# 
# | &nbsp; &nbsp; &nbsp; Polynomial &nbsp; &nbsp; &nbsp;|Coefficients|  
# |:---------:|:--:|
# |$8 - 6x + x^2$|`array([8, -6, 1])`|
# |$8 + x^2$|`array([8, 0, 1])`|
# |$- 6x + x^2$|`array([0, -6, 1])`|
# |$8$|`array([8])`|
# 

# **Use the `Polynomial` class defined below** for the following problems. 
# 
# **Add the following methods**:
# * **`__call__(x)`** evaluates the polynomial $P$ for a given value of $x$. It allows the use of the `P(x)` syntax. (You may use Horner's Method but it's not necessary.)
# * **`deriv()`** returns the derivative of $P(x)$ as a `Polynomial` with degree one less than $P$.
# 
# For example,
# ```
# poly = Polynomial([8, -6, 1])
# poly(-1)
# ```
# returns `15` and
# ```
# vars(poly.deriv())
# ```
# returns `{'coeffs': array([-6,  2]), 'degree': 1}`.
# 
# (*Optional:* You may add other methods to this class.)
# 
# 

# In[2]:


class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = np.array(coeffs)
        self.degree = self.coeffs.size - 1
    def __call__(self,x):
        x_vals = np.zeros(len(self.coeffs))
        deg1 = 0
        for i in range(len(self.coeffs)):
            x_vals[i] = x**deg1
            deg1 += 1
        return sum(x_vals*self.coeffs)
    def deriv(self):
        new_coeffs = np.zeros(len(self.coeffs) - 1)
        deg2 = 1
        for i in range(len(new_coeffs)):
            new_coeffs[i] = deg2*self.coeffs[i + 1]
            deg2 += 1
        return Polynomial(new_coeffs)


# In[3]:


poly = Polynomial([8, -6, 1])
poly(-1)


# In[4]:


vars(poly.deriv())


# ### Newton's Method for Polynomials

# Newton's Method is an iterative algorithm for finding a root of a differentiable function $f(x)$. Given an initial guess of $x_0$, the method converges to a solution by repeatedly applying this formula: 
# 
# $$ x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}.$$
# 
# When Newton's Method converges, it usually does so quickly, however it does not always converge, for example, when $f'(x_n) = 0$.
# 
# Write an iterative function **`newton(poly, x0, tol=1e-4, max_iter=50)`** that uses Newton's Method to find a root of a `Polynomial` $P(x)$ given an initial guess `x0`. The method terminates when $\lvert P(x_n)\rvert$ is less than the tolerance `tol`. If the method has not converged after `max_iter` iterations, the function returns `None`.

# In[5]:


def newton(poly, x0, tol=1e-4, max_iter=50):
    der = poly.deriv()
    iters = 1
    x1 = 0
    while abs(poly(x1)) >= tol:
        x1 = x0 - (poly(x0)/der(x0))
        x0 = x1
        iters += 1
    if iters > max_iter:
        return None
    else:
        return x1


# In[6]:


newton(poly,1)


# ### Recursive Newton's Method
# **Write a recursive version** of the previous function called **`newton_rec()`**.

# In[51]:


def newton_rec(poly, x0, tol=1e-4, max_iter=50, iters=1):
    der = poly.deriv()
    if abs(poly(x0)) >= tol:
        return newton_rec(poly,x0 - (poly(x0)/der(x0)),tol,max_iter,iters + 1)
    else:
        if iters > max_iter:
            return None
        else:
            return x0


# In[52]:


newton(poly,1)


# ### Bisection Method for Polynomials
# The *bisection method* is an alternate way to find a root of a `Polynomial`. Write a function **`bisection(poly, interval, tol=1e4, max_iter=50)`** that uses **binary search** to find a root of $P(x)$. Begin with a closed interval $[a, b]$ represented by a 2-element tuple `(a, b)`. If $P(a)$ and $P(b)$ are opposite signs, then a root is guaranteed to exist in interval $[a, b]$ because $P(x)$ is continuous. 
# 
# The method repeats these steps until a root is found (within the tolerance) or `max_iter` is reached:
# * Calculate the midpoint of the interval. If it corresponds to a root, return the root.
# * If the midpoint is not a root, repeat the process using either the left half or the right half of the interval.
# 
# The function returns `None` if $P(a)$ and $P(b)$ are not opposite signs.
# 
# (*Hint:* You may wish to use `np.sign(val)` which returns 1, 0, or -1, depending on whether `val` is positive, zero, or negative, respectively.)

# In[73]:


def bisection(poly, interval, tol=1e-4, max_iter=50, iters=1):
    mid = (interval[0] + interval[1])/2
    if poly(interval[0])*poly(interval[1]) < 0 and iters <= max_iter:
        if abs(poly(mid)) <= tol:
            return mid
        else:
            iters += 1
            if poly(interval[0])*poly(mid) < 0:
                return bisection(poly, (interval[0],mid), tol, max_iter, iters)
            else:
                return bisection(poly, (mid,interval[1]), tol, max_iter, iters)
    else:
        return None


# In[74]:


bisection(poly,(1,3))

