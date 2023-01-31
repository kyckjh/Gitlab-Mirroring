participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]

import random

class Participant:
    def __init__(self, num, couple, id):
        self.num = num          # 참가번호
        self.couple = couple    # 참가자의 짝
        self.id = id            # 참가자의 id
    def __str__(self):
        return f'{self.id:>2}번 참가자'

# 참가자 별로 랜덤한 id 부여
ids = list(range(1, len(participants)+1))   
random.shuffle(ids)

# 참가자 리스트 (class Participant를 element로 가짐)
part_list = []
while len(participants) > 0:
    num = participants.pop()
    try:
        id1 = ids.pop()
        part1 = Participant(num, None, id1)  # Participant 생성
        participants.remove(num)    # 같은 번호를 가진 짝 찾기, 짝이 없으면 ValueError
        id2 = ids.pop()
        part2 = Participant(num, part1, id2)  # 짝 Participant 생성, part1을 couple로 설정
        part2.couple = Participant(num, part2, id1)   # part1의 couple을 part2로 설정
        part_list.append(part2) 
        part_list.append(part2.couple)
    except ValueError:  # 짝이 없을 때 그냥 추가
        part_list.append(part1)
        
for p in part_list:
    #print(f'{p} 참가번호 : {p.num:>2}, 짝 : {p.couple}')
    if p.couple == None:    # 짝이 없는 참가자 찾기
        print(f'깍두기 : {p} 참가번호 {p.num}번')