# 로또 넘버 생성하기
# 로또 넘버 생성기
# 가져야 할 기능
# 무작위 번호 생성, 출력, 정렬
import random

class LottoNumberMaker:
    def __init__(self):
        self.lotto_number = set()
        
    def make_numbers(self):
        while len(self.lotto_number) < 6:
            self.lotto_number.add(random.randint(1,45))
    def print_numbers(self):
        print(self.lotto_number)
    def sort_numbers(self):
        self.lotto_number = list(self.lotto_number)
        self.lotto_number.sort()
        
    
maker = LottoNumberMaker()
# 랜덤한 숫자 생성
maker.make_numbers()
# 정렬
maker.sort_numbers()
# 출력
maker.print_numbers()