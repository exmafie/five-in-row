p1 = input(
    'Player 1 enter your name and your symbol for game separated by comma:')
p2 = input(
    'Player 2 enter your name and your symbol for game separated by comma:')

try:
    player1 = {p1.split(',')[0]: p1.split(',')[1]}
    print('Welcome {}, your symbol for the game is {}'.format(
        p1.split(',')[0], p1.split(',')[1]))
    player2 = {p2.split(',')[0]: p2.split(',')[1]}
    print('Welcome {}, your symbol for the game is {}'.format(
        p2.split(',')[0], p2.split(',')[1]))
except IndexError:
    print('Enter only two values and separate them with comma')
