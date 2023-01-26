lst = [0,1,2,3,4,5,6,7,8,9]
N = input()
set_num = 1
for n in N:
    n = int(n)
    try:
        lst.remove(n)
    except:
        if n == 6:
            try:
                lst.remove(9)
            except:
                lst += [0,1,2,3,4,5,6,7,8,9]
                set_num += 1
        elif n == 9:
            try:
                lst.remove(6)
            except:
                lst += [0,1,2,3,4,5,6,7,8,9]
                set_num += 1
        else:
            lst += [0,1,2,3,4,5,6,7,8,9]
            lst.remove(n)
            set_num += 1
print(set_num)