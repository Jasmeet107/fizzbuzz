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

def main():
    still_playing = True 
    count = 1
    player_turn = bool(random.getrandbits(1))
    prob = .7
    set_difficulty = False
    print ('Welcome to fizzbuzz. We are going to take turns counting, starting with 1. But it is not so simple! '
    'If your number is divisible by 3, write "fizz". If your number is divisible by 5, write "buzz". '
    'If your number is divisible by both 3 and 5, write "fizzbuzz". If you write the wrong thing, or '
    'you hesitate, you will lose the game! I can also lose the game.')
    difficulty = raw_input('Please choose my difficulty: (easy/med/hard) ')
    while not set_difficulty:
        if difficulty == 'easy': 
            prob = .7
            set_difficulty = True
        elif difficulty == 'med': 
            prob = .8
            set_difficulty = True
        elif difficulty == 'hard': 
            prob = .95
            set_difficulty = True
        else: 
            difficulty = raw_input('Invalid input! Please write "easy", "med", or "hard. ')
    while still_playing: 
        if player_turn: 
            guess = raw_input('Your turn! ')
            if guess != evaluate(count):
                print 'Sorry, that is incorrect! Game over.'
                still_playing = False
                break
            else: 
                player_turn = False
                count += 1
                continue
        else: 
            guess = answer(count, prob)
            print guess
            if guess != evaluate(count):
                print 'Looks like I messed up! You win!'
                still_playing = False
                break
            else: 
                player_turn = True
                count +=1
                continue
    print 'Thanks for playing!'

if __name__ == '__main__': 
    main()

