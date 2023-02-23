def calc_alphabet():
    pass


def permutation(i, k):
    if i == k:
        calc_alphabet()
    for a in range(i, k-1):
        for b in range(a+1, k):
            arr[a], arr[b] = arr[b], arr[a]
            permutation(i+1, k)
            arr[a], arr[b] = arr[b], arr[a]


alpha_num = 7 # 알파벳 종류
arr = list(range(1, alpha_num+1))
N = int(input())
data = [input() for _ in range(N)]
