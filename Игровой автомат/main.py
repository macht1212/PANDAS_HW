from numpy import random
import re

players_money = 1000000
wins = 0

win = {
    '777': 200,
    '999': 100,
    '555': 50,
    '333': 15,
    '111': 10
}

count = 0


def play():
    """The function removes 1 CU from the player's account at the beginning of the game"""
    global players_money
    players_money -= 1


def number():
    """The function generates a random number of 3 digits"""
    num = []
    x = random.randint(0, 10, 3)
    for i, el in enumerate(x):
        a = str(x[i])
        num.append(a)

    return ''.join(num)


def check(res):
    """The function checks the received number for a possible win and, in case of victory, adds the winnings to the
    player's account """
    global players_money, wins
    for key, value in win.items():
        if res == key:
            players_money += value
            wins += 1
    if re.findall(r'[123456789][123456789]0', res):
        players_money += 1
        wins += 1
    elif re.findall(r'[123456789]00', res):
        players_money += 2
        wins += 1
    elif re.findall(r'[012345689][012345689]7', res):
        players_money += 3
        wins += 1
    elif re.findall(r'[012345689]77', res):
        players_money += 5
        wins += 1


while players_money != 0:
    count += 1
    play()
    res = number()
    check(res)
    print(res)
    print(f'Your score {players_money}\n')
    if players_money == 0:
        print('You lose all money!')
        print(f'You had {count} games')
        print(f'You won {wins} times per all games')
        print(f'Conversion is {(wins/count)*100}%')

