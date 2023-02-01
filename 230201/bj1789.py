N = int(input())
k = 1
while True:
    sum = (k * (k + 1))/2
    if sum > N:
        break
    else:
        k += 1
print(k - 1)