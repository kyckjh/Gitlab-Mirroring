cnt = 0
salt = 0    # 총 소금의 양(g)
water = 0   # 총 물의 양 (g)
while(cnt < 5):
    str_input = input()
    if(str_input == 'Done'):
        break
    con, amount = map(int, str_input.split()) # 농도, 양
    salt_temp = amount * con / 100  # 현재 용액의 소금 양 (g)
    salt += salt_temp
    water += amount - salt_temp
    cnt += 1
    
print(f'퍼센트농도 : {salt / (salt + water) * 100:.2f}%   양 : {salt + water:.2f}g')
    
