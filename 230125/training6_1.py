# A. 입력예시

def de_identify(id):
    return id[:6] + '*' * 7
    
print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 
