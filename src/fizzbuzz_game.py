import os
import sys

sys.path.insert(0, os.getcwd())

def evaluate(count): 
    if count%3 == 0 and count%5 == 0:
        return 'fizzbuzz'
    if count%3 == 0: 
        return 'fizz'
    if count%5 == 0:
        return 'buzz'
    return str(count)

