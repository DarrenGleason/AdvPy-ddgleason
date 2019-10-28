#Darren Gleason
#Parsing Hex - 3.0

import sys

makesure = set('0123456789abcdef')

for real in sys.stdin.readlines():
    fullline = real.lower()
    i = 0
    while i < len(fullline) - 1:
        if fullline[i] == '0' and fullline[i+1] == 'x':
            num = ''
            for j in range(i+2, len(fullline)):
                if fullline[j] not in makesure:
                    break
                num += real[j]
            if len(num) > 0:
                dec = int(num, base=16)
                print('{}{}{} {}'.format(real[i],
                                        real[i+1],
                                         num,
                                         dec))
        i += 1