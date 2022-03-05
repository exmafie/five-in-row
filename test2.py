kobliha = []
letters = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
for l in range(10+1):
    test_list = []
    for i in range(10+1):
        if i == 0:
            test_list.insert(1, letters[l])
        elif l == 0:
            test_list.append(i)
        else:
            test_list.append('-')
    print(*test_list, sep='   ')
    kobliha.append(test_list)
# print(*kobliha, sep=' ')
