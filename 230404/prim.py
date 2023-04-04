'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

def push(queue, key_idx, value):
    queue.append(value)
    idx = len(queue)-1
    while idx != 0:
        if queue[idx//2][key_idx] < queue[idx][key_idx]:
            queue[idx // 2], queue[idx] = queue[idx], queue[idx // 2]
            idx //= 2
        else:
            break
    # return queue

def pop(queue, key_idx):
    parent = 0
    queue[0] = queue[-1]
    queue.pop()
    child = parent*2
    while child < len(queue):
        if child+1 < len(queue):
            if queue[child][key_idx] < queue[child+1][key_idx]:
                child += 1
        if queue[child][key_idx] > queue[parent][key_idx]:
            queue[child], queue[parent] = queue[parent], queue[child]
            parent = child
        else:
            break


V, E = map(int, input().split())
adj = [[0] * (V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    adj[a][b] = w
    adj[b][a] = w
# 인접행렬 완성
def prim(graph, V, start):
    mst = set() # MST에 포함된 노드를 넣을 set
    # 강의 자료에서 pi와 key에 해당하는 데이터는
    # pi : 어느 정점으로부터 선택되었나를 저장하는 값
    # key : 해당 정점을 선택하는 가중치
    pi = [None]*(V+1)
    weight = [0xffffffff]*(V+1)
    # 시작정점 잡아주기
    weight[start] = 0
    # 최소 가중치를 가지는 정점을 선택하는 것을 반복
    # >> 모든 정점이 선택될 때 까지 반복
    while len(mst) < V+1:
        # 최소 가중치 선택하기
        # 아직 선택되지 않은 노드이면서 최소 가중치라면 선택
        min_v = 0xffffffff
        min_idx = 0
        for i in range(V+1):
            if i not in mst and weight[i] < min_v:
                min_v = weight[i]
                min_idx = i
        # 최소값 구하기 종료
        mst.add(min_idx)
        # min_idx번 노드가 선택되었으므로
        # min_idx에서 갈 수 있는 정점까지 가중치가 더 작다면 업데이트
        for i in range(V+1):
            # weight[i]가 min_idx에서 i번으로 가는 비용보다 더 크다면
            # 아직 i가 mst에 포함되지 않으면서
            # min_idx랑 i랑 연결되어 있는지 확인
            if i not in mst and adj[min_idx][i] \
                    and weight[i] > adj[min_idx][i]:
                weight[i] = adj[min_idx][i]
                pi[i] = min_idx
    return (pi, weight)

result = prim(adj, V, 0)
for row in result:
    print(row)