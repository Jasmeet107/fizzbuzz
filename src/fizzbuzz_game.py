import os
import random
import signal
import sys

sys.path.insert(0, os.getcwd())

##I don't quite get what this is necessary for
class AlarmException(Exception):
    pass

def alarmHandler(signum, frame): 
    raise AlarmException

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
    difficulty_dict = {'easy': (.7, 9), 'med': (.8, 6), 'hard': (.95, 4)}
    still_playing = True 
    count = 1
    player_turn = bool(random.getrandbits(1))
    set_difficulty = False
    print ('Welcome to fizzbuzz. We are going to take turns counting, starting with 1. But it is not so simple! '
    'If your number is divisible by 3, write "fizz". If your number is divisible by 5, write "buzz". '
    'If your number is divisible by both 3 and 5, write "fizzbuzz". If you write the wrong thing, or '
    'you hesitate, you will lose the game! I can also lose the game.')
    difficulty = raw_input('Please choose my difficulty: (easy/med/hard) ')
    #is there a better way to do this?
    while not set_difficulty:
        if difficulty in difficulty_dict: 
            prob = difficulty_dict[difficulty][0]
            timeout = difficulty_dict[difficulty][1]
            set_difficulty = True
        else: 
            difficulty = raw_input('Invalid input! Please write "easy", "med", or "hard". ')
    while still_playing: 
        if player_turn: 
            signal.signal(signal.SIGALRM, alarmHandler)
            signal.alarm(timeout)
            try:
                guess = raw_input('Your turn! ')
                signal.alarm(0)
                if guess != evaluate(count):
                    print 'Sorry, that is incorrect! Game over.'
                    still_playing = False
                    break
                else: 
                    player_turn = False
                    count += 1
                    continue
            except AlarmException:
                print 'Sorry, you ran out of time! Game over.'
                signal.signal(signal.SIGALRM, signal.SIG_IGN)
                still_playing = False
                break
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

