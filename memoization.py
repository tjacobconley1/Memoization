#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:25:53 2021

MEMOIZED FIBONNACI

@author: fieldemployee
"""

def fastFib(n, memo = {}):
    """
    Assumes n is an int >= 0,
    memo used only by recursive calls
    Retutrns Fibonnaci of n
    MEMOIZATION - TRADING TIME FOR SPACE 
    """
    if n == 0 or n == 1:
        return 1
    try:
        # checks to see if the dictionary already
        # has the result of this iteration of fib
        # and if so it returns the already computed value 
        return memo[n]
    except KeyError:
        # if it is not already in the dictionary we
        # compute it 
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        print(result)
        # add the result to the dictionary 
        memo[n] = result
        # then return the result 
        return result

fastFib(120)
