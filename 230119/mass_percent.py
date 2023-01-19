cnt = 0
salt = 0.0    # 총 소금의 양(g)
water = 0.0   # 총 물의 양 (g)
while(cnt < 5):
    str_input = input('소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ')
    if(str_input == 'Done'):
        break
    input1, input2 = str_input.split() # 농도, 양
    con = float(input1[0:-1])
    amount = float(input2[0:-1])
    print(con, amount)
    salt_temp = amount * con / 100  # 현재 용액의 소금 양 (g)
    salt += salt_temp
    water += amount - salt_temp
    cnt += 1
    
print(f'{round(salt / (salt + water) * 100, 2)}% {round(salt + water, 2)}g')
