T = int(input())
for t in range(1, T+1):
    s = input()
    l = len(s)
    print('.', end='')
    for i in range(l):
        print('.#..', end='')
    print()

    print('.', end='')
    for i in range(l):
        print('#.#.', end='')
    print()

    print('#', end='')
    for i in range(l):
        print(f'.{s[i]}.#', end='')
    print()

    print('.', end='')
    for i in range(l):
        print('#.#.', end='')
    print()

    print('.', end='')
    for i in range(l):
        print('.#..', end='')
    print()