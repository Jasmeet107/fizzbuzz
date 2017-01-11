import os
import random
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

def answer(count, probability):
    arbitor = (random.random() < probability)
    if count%3 == 0 and count%5 == 0:
        return 'fizzbuzz' if arbitor else random.choice([str(count), 'fizz', 'buzz'])
    if count%3 == 0: 
        return 'fizz' if arbitor else random.choice([str(count), 'buzz', 'fizzbuzz'])
    if count%5 == 0:
        return 'buzz' if arbitor else random.choice([str(count), 'fizz', 'fizzbuzz'])
    return str(count) if arbitor else random.choice(['fizz', 'buzz', 'fizzbuzz'])

