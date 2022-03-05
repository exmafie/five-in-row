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

length = int(input('Enter the length of field (min 5,max10): '))
width = int(input('Enter the width of field (min 5,max10): '))

field = []


def size_of_field(width, length):

    letters = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for l in range(length+1):
        test_list = []
        for i in range(width+1):
            if i == 0:
                test_list.insert(1, letters[l])
            elif l == 0:
                test_list.append(i)
            else:
                test_list.append('-')
        print(*test_list, sep='   ')
        field.append(test_list)
    return field


size_of_field(length, width)

# print(field)
