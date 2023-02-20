def f(i, k):
   if i == k:
       print(p)
   else:
       for j in range(i, k):
           p[i], p[j] = p[j], [i]
           f(i+1, k)
           p[i], p[j] = p[j], [i]


p = [1,2,3]
N = len(p)
f(1, N)