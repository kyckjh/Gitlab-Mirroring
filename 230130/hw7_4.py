class Colla:
    def func1(num):
        return num // 2
    def func2(num):
        return num * 3 + 1    

def collatz(num):
    cnt = 0
    while num != 1 and cnt < 500:
        if num % 2:
            num = Colla.func2(num)
        else:
            num = Colla.func1(num)
        cnt += 1
    return cnt if cnt < 500 else -1

print(collatz(6)) #=> 8
print(collatz(16)) #=> 4
print(collatz(27)) #=> 111
print(collatz(626331)) #=> -1