class Pizza:
    def __init__(self, num, cheese):
        self.num = num
        self.cheese = cheese

class Oven:
    def __init__(self, size):
        self.size = size
        self.plate = [None]*size
        self.__front = self.__rear = 0

    def In(self, pizza): # 피자 넣기
        self.rear += 1
        self.plate[self.rear] = pizza

    def Out(self): # 피자 꺼내기
        self.front += 1
        self.plate[self.front].cheese //= 2 # 피자 치즈가 절반이 됨
        return self.plate[self.front]

    def get_first_pizza(self):
        self.front += 1
        return self.plate[self.front].num + 1

    def is_last_one(self):
        return (self.__front + 1) % self.size == self.rear

    @property
    def front(self):
        return self.__front

    @front.setter
    def front(self, front):
        self.__front = front % self.size

    @property
    def rear(self):
        return self.__rear

    @rear.setter
    def rear(self, rear):
        self.__rear = rear % self.size

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    oven = Oven(N)
    arr = list(map(int, input().split()))
    for i in range(N):   # 화덕이 꽉 찰 때 까지 피자 넣기(N번)
        oven.In(Pizza(i, arr[i]))   # (피자 번호, 남은 치즈 양)

    idx = N   # 대기중인 남은 피자 번호
    while not oven.is_last_one():        # 피자가 하나 남았을 때 반복문 탈출
        pizza = oven.Out()        # 피자 꺼내기
        if pizza.cheese == 0:     # 피자 치즈가 다 녹았으면
            if idx < M:           # 아직 넣지 않고 남은 피자가 있으면
                oven.In(Pizza(idx, arr[idx]))    # 다음 피자 넣기
                idx += 1          # 피자 대기번호 증가
        else:     # 피자치즈가 다 녹지 않았으면
            oven.In(pizza)  # 피자 다시 넣기

    print(f'#{t} {oven.get_first_pizza()}')   # 마지막 남은 피자의 번호 출력