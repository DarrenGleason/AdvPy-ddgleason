# Darren Gleason
# Bing it on - Difficulty 3.9

import sys

def main():
    readin = sys.stdin.readline
    dict = {}
    number = int(readin())
    
    for _ in range(number):
        word = readin().strip()
        element = dict

        for char in word:
            if char in element:
                element[char][0] += 1
            else:
                element[char] = [0, {}]
            answer = element[char][0]
            element = element[char][1]
        print(answer)

main()