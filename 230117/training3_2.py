str_input = input()
length = len(str_input)
if length % 2:
    print(str_input[(length+1)//2-1])
else:
    print(str_input[(length+1)//2 - 1],str_input[(length+1)//2])