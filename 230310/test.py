arr=[]
for _ in range(5):
    arr.append(int(input()))
b = arr[2]//arr[4]
if arr[2]%arr[4]!=0:
    b+=1
c = arr[1]//arr[3]
if arr[1]%arr[3]!=0:
    c+=1
print(arr[0]-max(b, c))