import sys
while True:
    s = sys.stdin.readline()
    if '#' in s:
        break
    s = s.lower()
    print(s)
    ans = s.count('a')
    ans += s.count('e')
    ans += s.count('i')
    ans += s.count('o')
    ans += s.count('u')
    print(ans)
    