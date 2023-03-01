#!/usr/bin/env python
# coding: utf-8

# # HW 1
# 
# **Upload two files** to Gradescope: 
# * `HW1.ipynb` (run all cells to make sure that outputs are visible, especially plots)
# * `HW1.py` (which will be autograded)
# 
# ___

# In[1]:


import math
import matplotlib.pyplot as plt
import numpy as np


# ### Fractions
# 
# Create a **`Fraction`** class to represent fractions as objects. The **`__init__`** method should do the following:
# * Store the numerator and denominator as separate attributes. Assume that they are `int`s.
# * Set the default value for the denominator to be 1.
# * If the fraction is negative, set the numerator to be negative. 
# * Generate an error if the denominator is 0 by calling `raise ZeroDivisionError('division by zero')`.
# * The fraction should be stored in simplest form. Use the `math.gcd()` function.
# 
# Include the following methods. For arithmetic operations, return a `Fraction` in simplest form.
# * **`__repr()__`**: returns a string representation of a `Fraction` in the form `numerator/denominator` with no spaces. 
# * **`__eq__()`**: returns `True` if two `Fraction`s are equal
# * **`__add__()`**: adds two `Fraction`s
# * **`__sub__()`**: subtracts two `Fraction`s
# * **`__mul__()`**: multiplies two `Fraction`s
# * **`__truediv__()`**: divides two `Fraction`s (raise an error if the second fraction is zero)
# * **`plot()`**: uses a row of colored rectangles to illustrate a `Fraction` with value between 0 and 1. If the `Fraction` value is greater than 1, display only the remainder part.
# 
# Examples:<br>
# `Fraction(3, 5)` returns a `Fraction` and displays the string `3/5`.<br>
# `Fraction(6, -10)` returns a `Fraction` and displays the string `-3/5`.<br>
# `Fraction(-3, 5) == Fraction(6, -10)` returns `True`.<br>
# `Fraction(3, 5) + Fraction(7, 5)` returns a `Fraction` and displays the string `2/1`.<br>
# `Fraction(2, 5) - Fraction(3, 5)` returns a `Fraction` and displays the string `-1/5`.<br>
# `Fraction(3, 5) * Fraction(5, 6)` returns a `Fraction` and displays the string `1/2`.<br>
# `Fraction(3, 5) / Fraction(5, 6)` returns a `Fraction` and displays the string `18/25`.<br>
# `Fraction(17, 5).plot()` displays a row of 5 rectangles with 2 of the rectangles shaded, representing the value 2/5.
# 
# <img src="http://www.coloradomath.org/python/fracplot.jpg" width="259" height="69" />

# In[2]:


class Fraction:
    def __init__(self, n, d=1):
        self.num = int(n / math.gcd(abs(n), abs(d)))
        self.den = int(d / math.gcd(abs(n), abs(d)))
        if self.den < 0:
            self.den = abs(self.den)
            self.num = -1*self.num
        elif self.den == 0:
            raise ZeroDivisionError('division by zero')
        
    def __repr__(self):
        return str(self.num) + "/" + str(self.den)
    def __eq__(self, other):
        return self.num == other.num and self.den == other.den
    def __add__(self, other):
        return Fraction(self.num*other.den + self.den*other.num, self.den*other.den)
    def __sub__(self, other):
        return Fraction(self.num*other.den - self.den*other.num, self.den*other.den)
    def __mul__(self, other):
        return Fraction(self.num*other.num, self.den*other.den)
    def __truediv__(self, other):
        return Fraction(self.num*other.den, self.den*other.num)
    def plot(self):
        if self.num > self.den:
            Fraction(self.num - self.den, self.den).plot()
        else:
            x = np.linspace(0,self.den,100)
            y = np.linspace(0,1,100)
            z = np.zeros(100)
            o = np.zeros(100) + 1
            plt.plot(x,z,'k')
            plt.plot(x,o,'k')
            for i in range(self.den + 1):
                j = np.zeros(100) + i
                plt.plot(j,y,'k')
            for k in range(self.num):
                x1 = np.linspace(k,k + 1,100)
                y1 = np.zeros(100) + 1
                plt.fill_between(x1,y1,color='aqua')
            plt.axis('off')
            plt.axis('equal')
            plt.show()

Fraction(17, 5).plot()


# In[3]:


Fraction(3, 5) / Fraction(5, 6)


# ### Unit Fractions
# 
# A *unit fraction* has a numerator of 1. Create a **UnitFraction** subclass that inherits all of the properties of the `Fraction` class.
# 
# Example:<br>
# `UnitFraction(2) * UnitFraction(3)` returns a Fraction object and displays the string `1/6`.<br>
# `UnitFraction(2) == Fraction(3, 6)` returns `True`.

# In[4]:


class UnitFraction(Fraction):
    def __init__(self,d):
        super().__init__(1,d)


# In[5]:


UnitFraction(2) * UnitFraction(3)


# ### Egyptian Fractions
# An *Egyptian fraction* is a representation of a fraction as a sum of distinct unit fractions, such as $\frac 56 = \frac 12 + \frac 13$. Fibonacci's *greedy algorithm* can find an Egyptian fraction representation for any fraction $\frac ab$ by repeatedly choosing the largest possible unit fraction. For example, applying the algorithm to the fraction $\frac {7}{15}$ produces
# 
# $$\frac{7}{15} = \frac 13 + \frac{2}{15} = \frac 13 + \frac 18 + \frac{1}{120}.$$
# 
# Note that the greedy algorithm does not always find the shortest representation. For example, $\frac{4}{17}$ equals $\frac 15 + \frac{1}{30} + \frac{1}{510}$ with 3 unit fractions, however the greedy algorithm produces 4.
# 
# Write a non-recursive function **egyptian(frac)** that returns a list of the `UnitFraction`s that sum to a given positive `Fraction`. If the fraction is greater than 1, the first element of the list should be an integer `Fraction`. (Can you figure out how to find the largest unit fraction at each step?) 
# 
# Example:<br>
# `egyptian(Fraction(7, 15))` returns a list of 3 `UnitFraction`s and displays `[1/3, 1/8, 1/120]`.<br>
# `egyptian(Fraction(17, 6))` returns a list containing a `Fraction` and two `UnitFraction`s, displaying `[2/1, 1/2, 1/3]`.<br>
# `egyptian(Fraction(3))` returns a list containing a single `Fraction`, displaying `[3/1]`.

# In[6]:


def egyptian(frac):
    lst = []
    number = frac.num/frac.den
    if number > 1:
        n = math.floor(number)
        lst.append(Fraction(n))
        frac.num = frac.num - n*frac.den
    while frac.num > 0:
        f = frac.num/frac.den
        count = 2
        while f < 1/count:
            count = count + 1
        lst.append(UnitFraction(count))
        newfrac = Fraction(frac.num,frac.den) - Fraction(1,count)
        frac.den = newfrac.den
        frac.num = newfrac.num
    return lst


# In[7]:


egyptian(Fraction(17, 6))


# Now write a recursive version called **egyptian_rec(frac)**.

# In[8]:


def egyptian_rec(frac, c=1, lst=[]):
    if c == 1:
        lst = []
    number = frac.num/frac.den
    if number > 1:
        n = math.floor(number)
        lst.append(Fraction(n))
        frac.num = frac.num - n*frac.den
        c = c + 1
        egyptian_rec(frac,c,lst)
    elif frac.num > 0:
        f = frac.num/frac.den
        count = 2
        while f < 1/count:
            count = count + 1
        lst.append(UnitFraction(count))
        newfrac = Fraction(frac.num,frac.den) - Fraction(1,count)
        c = c + 1
        egyptian_rec(newfrac,c,lst)
    return lst


# In[9]:


egyptian_rec(Fraction(7, 15))

