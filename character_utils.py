import random

__author__ = 'Glenn'

def roll4d6():
    """
    Rolls four random numbers between 1 through 6, removes lowest of the four, then uses sum()
    to total the rolls
    Returns : int the sum of the three highest numbers
    """
    rollList = [random.randint(1,6) for i in range(4)]
    rollList.remove(min(rollList))
    return sum(rollList)

