# Darren Gleason
# Bit by Bit - Difficulty 2.9
import sys

while True:
    inn = input().rstrip()
    if inn == '0':
        break

    if inn.isdigit() is True:
        all_values = int(inn) + 1
        bit = ['?'] * 32
        while all_values > 1:
            value = input().split()
            i = int(value[1])
            all_values -= 1
            if value[0] == 'SET':
                bit[31 - i] = '1'
                continue
            
            if value[0] == 'CLEAR':
                bit[31 - i] = '0'
                continue

            if value[0] == 'AND':
                j = int(value[2])
                if bit[31 - i] == '?' and bit[31 - j] == '?':
                    bit[31 - i] = '?'
                elif bit[31 - i] == '?' or bit[31 - j] == '?':
                    bit[31 - i] = '0' if bit[31 - i] == '0' or bit[31 - j] == '0' else '?'
                else:
                    bit[31 - i] = '1' if bit[31 - i] == '1' and bit[31 - j] == '1' else '0'
                continue

            if value[0] == 'OR':
                    j = int(value[2])
                    if bit[31 - i] == '?' and bit[31 - j] == '?':
                        bit[31 - i] = '?'
                    elif bit[31 - i] == '?' or bit[31 - j] == '?':
                        bit[31 - i] = '1' if bit[31 - i] == '1' or bit[31 - j] == '1' else '?'
                    else:
                        bit[31 - i] = '1' if bit[31 - i] == '1' or bit[31 - j] == '1' else '0'
                    continue
        answer = ''.join(bit)
        print(answer)