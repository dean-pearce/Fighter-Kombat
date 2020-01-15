# Introduction
from pip._vendor.distlib.compat import raw_input

print("FIGHTER KOMBAT-ish")
print("--- First Player ---")
while True:
    name = 'Type Your Player`s name: '
    player1 = raw_input(name)
    if len(player1) <= 2:
        print('Error, Name Must Be At Least 3 Letters')
    else:
        break
print("--- Second Player ---")
while True:
    name2 = 'Type Your 2nd Player`s name: '
    player2 = raw_input(name2)
    if len(player2) <= 2:
        print('Error, Name Must Be At Least 3 Letters')
    elif player2 == player1:
        print('Error, Name Must Be Different From First Player`s')
    else:
        break
print('Game Starting....')
print('')
print('')

# ------------------------------------------------------------

# Coin Toss
import random

coin = random.randint(1, 2)
if coin == 1:
    print(player1, 'Starts First!')
if coin == 2:
    print(player2, 'Starts First!')

print('')
print('')


def coin_toss():
    coin = random.randint(1, 2)

    if coin == 1:
        print(player1, 'Starts First!')
    if coin == 2:
        print(player2, 'Starts First!')

    print('')
    print('')


# -------------------------------------------------------------

# HP
hp1 = 100
hp2 = 100
a = str(int(hp1 / 2) * '|')
b = str(int(hp2 / 2) * '|')


def hp():
    if coin == 1:
        print(player1, 'HP[' + str(hp1) + "]:" + str(a), '  ', )
        print(player2, 'HP[' + str(hp2) + "]:" + str(b))
    if coin == 2:
        print(player2, 'HP[' + str(hp2) + "]:" + str(b), '  ', )
        print(player1, 'HP[' + str(hp1) + "]:" + str(a))


# ------------------------------------------------------------------------

# Gameplay

chance = random.randint(0, 100)


def killing():
    hp1 = 100
    hp2 = 100
    if coin == 1:
        while True:
            a = str(int(hp1 / 2) * '|')
            b = str(int(hp2 / 2) * '|')
            if int(hp1) == 0 or str(a) == '':
                print(player2, 'Wins!!')
                break
            if int(hp2) == 0 or str(b) == '':
                print(player1, 'Wins!!')
                break
            else:
                attack = raw_input('1st Player Attack: ')
                hit = 100 - int(attack)
                miss = random.randint(0, 100)
                if int(attack) > int(50):
                    print('attack is between 0 and 50')
                    continue
                if miss > hit:
                    print('Oops You Missed.')
                    print('')
                elif miss < hit:
                    print(player1, 'hits with', attack, 'damage')
                    print('')
                    hp2 = int(hp2) - int(attack)
                a = str(int(hp1 / 2) * '|')
                b = str(int(hp2 / 2) * '|')
                print(player1, 'HP[' + str(hp1) + "]:" + str(a), '  ', )
                print(player2, 'HP[' + str(hp2) + "]:" + str(b), '  ')
                if int(hp1) == 0 or str(a) == '':
                    print(player2, 'Wins !!')
                    break
                if int(hp2) == 0 or str(b) == '':
                    print(player1, 'Wins !!')
                    break
                attack = raw_input('2nd Player Attack: ')
                hit = 100 - int(attack)
                miss = random.randint(0, 100)
                if int(attack) > int(50):
                    print('attack is between 0 and 50')
                    continue
                if miss > hit:
                    print('Oops You Missed.')
                    print('')
                elif miss < hit:
                    print(player2, 'hits with', attack, 'damage')
                    print('')
                    hp1 = int(hp1) - int(attack)
                a = str(int(hp1 / 2) * '|')
                b = str(int(hp2 / 2) * '|')
                print(player1, 'HP[' + str(hp1) + "]:" + str(a), '  ', )
                print(player2, 'HP[' + str(hp2) + "]:" + str(b), '  ')
                if int(hp1) == 0 or str(a) == '':
                    print(player2, 'Wins !!')
                    break
                if int(hp2) == 0 or str(b) == '':
                    print(player1, 'Wins !!')
                    break

    if coin == 2:
        while True:
            a = str(int(hp1 / 2) * '|')
            b = str(int(hp2 / 2) * '|')
            if int(hp1) == 0 or str(a) == '':
                print(player2, 'Wins !!')
                break
            if int(hp2) == 0 or str(b) == '':
                print(player1, 'Wins !!')
                break
            else:
                attack = raw_input('2nd Player Attack: ')
                hit = 100 - int(attack)
                miss = random.randint(0, 100)
                if int(attack) > int(50):
                    print('attack is between 0 and 50')
                    continue
                if miss > hit:
                    print('Oops You Missed.')
                    print('')
                elif miss < hit:
                    print(player2, 'hits with', attack, 'damage')
                    print('')
                    hp1 = int(hp1) - int(attack)
                a = str(int(hp1 / 2) * '|')
                b = str(int(hp2 / 2) * '|')
                print(player2, 'HP[' + str(hp2) + "]:" + str(b), '  ', )
                print(player1, 'HP[' + str(hp1) + "]:" + str(a))
                if int(hp1) == 0 or str(a) == '':
                    print(player2, 'Wins !!')
                    break
                if int(hp2) == 0 or str(b) == '':
                    print(player1, 'Wins !!')
                    break
                attack = raw_input('1st Player Attack: ')
                hit = 100 - int(attack)
                miss = random.randint(0, 100)
                if int(attack) > int(50):
                    print('attack is between 0 and 50')
                    continue
                if miss > hit:
                    print('Oops You Missed.')
                    print('')
                elif miss < hit:
                    print(player1, 'hits with', attack, 'damage')
                    print('')
                    hp2 = int(hp2) - int(attack)
                a = str(int(hp1 / 2) * '|')
                b = str(int(hp2 / 2) * '|')
                print(player2, 'HP[' + str(hp2) + "]:" + str(b), '  ', )
                print(player1, 'HP[' + str(hp1) + "]:" + str(a))
                if int(hp1) == 0 or str(a) == '':
                    print(player2, 'Wins !!')
                    break
                if int(hp2) == 0 or str(b) == '':
                    print(player1, 'Wins !!')
                    break


# --------------------------------------
# ResetGame
def restart():
    while True:
        reset = raw_input('Would You Like To Restart The Game? (True/False)')
        if reset == 'True':
            print('Restarting Game')
            print('')
            print('')
            coin_toss()
            hp()
            killing()
        if reset == 'False':
            print('Thank You For Playing FIGHTER KOMBAT')
            break


hp()
killing()
restart()
