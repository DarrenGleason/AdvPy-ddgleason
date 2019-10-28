# Darren Gleason
# Digital Display - Difficulty 2.5
g = ['' for _ in range(10)]
g[0] = ["+---+", "|   |", "|   |", "+   +", "|   |", "|   |", "+---+"]
g[1] = ["    +", "    |", "    |", "    +", "    |", "    |", "    +"]
g[2] = ["+---+", "    |", "    |", "+---+", "|    ", "|    ", "+---+"]
g[3] = ["+---+", "    |", "    |", "+---+", "    |", "    |", "+---+"]
g[4] = ["+   +", "|   |", "|   |", "+---+", "    |", "    |", "    +"]
g[5] = ["+---+", "|    ", "|    ", "+---+", "    |", "    |", "+---+"]
g[6] = ["+---+", "|    ", "|    ", "+---+", "|   |", "|   |", "+---+"]
g[7] = ["+---+", "    |", "    |", "    +", "    |", "    |", "    +"]
g[8] = ["+---+", "|   |", "|   |", "+---+", "|   |", "|   |", "+---+"]
g[9] = ["+---+", "|   |", "|   |", "+---+", "    |", "    |", "+---+"]

# def bad():
#     print('You cannot have negative time!!')

while True:
    inn = input()
    if inn == 'end':
        print('end')
        break

    for y in range(7):
        output = ''
        for q in inn:
            # if q <= '-1':
            #     y = 0
            #     bad()
            #     break
            if q == ':':
                if y == 2 or y == 4:
                    output += 'o'
                else:
                    output += ' '
            else:
                q = int(q)
                for x in range(5):
                    output += g[q][y][x]
            output += '  '
        print(output[:-2])
    print()
    print()
