a = 3
b = 6
c = -5
import math
x, y = ((-b) + math.sqrt(b*b - 4*a*c))/(2*a), ((-b) - math.sqrt(b*b - 4*a*c))/(2*a)
np_a = '-' if a < 0 else ''
np_b = '-' if b < 0 else '+'
np_c = '-' if c < 0 else '+'
print(f'{np_a}{-a if a<0 else a}x^2 {np_b} {-b if b<0 else b}x {np_c} {-c if c<0 else c}')
print((round(x,4), round(y,4)))