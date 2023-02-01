class PublicTransport:
    def __init__(self, name, fare):
        self.name = name    # 이름
        self.fare = fare    # 요금
        self.passengers_now = 0     # 현재 탑승자수
        self.passengers_all = 0     # 누적 탑승자수
        
    def get_in(self, num):  # 현재, 누적 탑승자수 증가
        self.passengers_now += num
        self.passengers_all += num
        
    def get_off(self, num): # 현재 탑승자수 감소
        self.passengers_now -= num
        
    def profit(self):   # 누적 탑승자수 X 요금
        return self.passengers_all * self.fare
    
class Bus(PublicTransport):
    def __init__(self, name, fare, limit):
        super().__init__(name, fare)
        self.limit = limit
    
    def get_in(self, num):    
        if self.passengers_now + num > self.limit:
            raise Exception("더이상 탑승할 수 없습니다.")
        else:
            super().get_in(num)
        
    
bus = Bus('버스', 1500, 5)
bus.get_in(5)
print(bus.passengers_now)
bus.get_in(2)
print(bus.passengers_now)
bus.get_off(1)
bus.get_off(4)
bus.get_in(3)
print(bus.passengers_now)
bus.get_in(1)
print(bus.profit())
