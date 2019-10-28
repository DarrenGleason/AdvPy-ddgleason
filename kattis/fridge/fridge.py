# Darren Gleason
# Fridge - Difficulty 3.3

inn = input()
r = {i:inn.count(str(i)) for i in range(10)}
digits = sorted(sorted(r.keys()), key = lambda x: r[x])

finish = False
for i in range(1, 10):
    if r[i] == 0:
        print(i)
        finish = True
        break

if not finish:
    leastcomnum = digits[0]
    if leastcomnum == 0:
        if r[0] < r[digits[1]]:
            print('1' + '0'*(r[0]+1))
            finish = True
        else:
            leastcomnum = digits[1]
    if not finish:
        print(str(leastcomnum)*(r[leastcomnum]+1))