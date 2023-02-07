a = input()
result = 0
cros = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=', 'dz=']
for cro in cros:
    result += a.count(cro)
print(len(a) - result)