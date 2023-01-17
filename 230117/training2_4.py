# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500

stake = 50000
VAT = stake * 15 // 100

print(f'스테이크    {stake:,}')
print(f'+ VAT       {VAT:,}')
print(f'총계 ₩      {stake + VAT:,}')