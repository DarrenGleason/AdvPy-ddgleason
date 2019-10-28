# Darren Gleason
# ToLower - Difficulty 1.8

problems, testcases = map(int, input().split())

solved = 0
for _ in range(problems):
        s = [input().strip() for _ in range(testcases)]
        if all(t[0].lower() + t[1:] == t.lower() for t in s):
                solved += 1
print(solved)

