orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
order_list = orders.split(',')
iceNum = 0
order_dict = {}
for order in order_list:
    if(order.find('아이스') == False):
        iceNum += 1
    if(order_dict.get(order) == None):
        order_dict[order] = 1
    else:
        order_dict[order] += 1
    
print(f'아이스 음료 주문은 {iceNum}건 들어왔습니다.')
for order in order_dict:
    print(f'{order} : {order_dict[order]}개')