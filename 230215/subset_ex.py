arr = [1,2,3,4,5]
N = len(arr)
selected = [0] * N

# idx에 해당하는 요소가 부분집합에 포함되는지 아닌지 결정
# 결정하고 나서 다음 요소 포함여부 결정하러 ㄱㄱ
def subset(idx):
    # 완전탐색 : 내가 할 수 있는거 다 해보면 됨

    if idx == N:
        print(selected)
        return
    selected[idx] = 1
    subset(idx + 1)
    selected[idx] = 0
    subset(idx + 1)

subset(0)