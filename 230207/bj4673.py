def selfnumber(n):
    sumN = n
    while n > 0:
        sumN += n % 10
        n //= 10
    return sumN

result = set(range(1, 10001))
sn_set = set()
for i in range(1, 10001):
    sn = selfnumber(i)
    if sn <= 10000:
        sn_set.add(sn)
result -= sn_set
result = list(result)
result.sort()
for n in result:
    print(n)