from numpy import random
import re

init_bank = 10000



win = {
    '777': 200,
    '999': 100,
    '555': 50,
    '333': 15,
    '111': 10
}




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
    global players_money, wins, wins777, wins999, wins555, wins333, wins111, wins0, wins00, wins7, wins77
    for key, value in win.items():
        if res == key:
            players_money += value
            wins += 1
            if key == '777':
                wins777 += 1
            elif key == '999':
                wins999 += 1
            elif key == '555':
                wins555 += 1
            elif key == '333':
                wins333 += 1
            elif key == '111':
                wins111 += 1
    if re.findall(r'[123456789][123456789]0', res):
        players_money += 1
        wins += 1
        wins0 += 1
    elif re.findall(r'[123456789]00', res):
        players_money += 2
        wins += 1
        wins00 += 1
    elif re.findall(r'[012345689][012345689]7', res):
        players_money += 3
        wins += 1
        wins7 += 1
    elif re.findall(r'[012345689]77', res):
        players_money += 5
        wins += 1
        wins77 += 1


for i in range(50):
    players_money = 10000
    wins = 0
    wins777 = 0
    wins999 = 0
    wins555 = 0
    wins333 = 0
    wins111 = 0
    wins0 = 0
    wins00 = 0
    wins7 = 0
    wins77 = 0
    count = 0
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
            print(f'Conversion is {(wins / count) * 100}%\n')
            print(f'777 was {wins777} times, frequency {wins777 / count}')
            print(f'999 was {wins999} times, frequency {wins999 / count}')
            print(f'555 was {wins555} times, frequency {wins555 / count}')
            print(f'333 was {wins333} times, frequency {wins333 / count}')
            print(f'111 was {wins111} times, frequency {wins111 / count}')
            print(f'**0 was {wins0} times, frequency {wins0 / count}')
            print(f'*00 was {wins00} times, frequency {wins00 / count}')
            print(f'**7 was {wins7} times, frequency {wins7 / count}')
            print(f'*77 was {wins77} times, frequency {wins77 / count}')

            with open('data.txt', 'a') as file:
                file.write(f'count,{count}\n')
                file.write(f'wins,{wins}\n')
                file.write(f'conversion,{(wins / count) * 100}\n')
                file.write(f'777,{wins777}\n')
                file.write(f'999,{wins999}\n')
                file.write(f'555,{wins555}\n')
                file.write(f'333,{wins333}\n')
                file.write(f'111,{wins111}\n')
                file.write(f'*77,{wins77}\n')
                file.write(f'**7,{wins7}\n')
                file.write(f'*00,{wins00}\n')
                file.write(f'**0,{wins0}\n')
