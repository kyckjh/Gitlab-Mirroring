
# 반복문 사용 X
def sum_of_digit(num):
    if num == 0:
        return 0
    return num % 10 + sum_of_digit(num//10)
        
print(sum_of_digit(3904)) # 16

# 반복문 사용
def sum_of_digit(num):
    sum = 0
    for i in range(len(str(num))):
        sum += num%10
        num //= 10
    return sum
    
print(sum_of_digit(3904)) # 16
