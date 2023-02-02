class Disk: # 원반
    def __init__(self, rad:int): # rad : 크기
        self.rad = rad
        
class Column:   # 기둥
    def __init__(self, name):
        self.name = name
        self.disks = []
        
    def disk_in(self, disk:Disk):
        if len(self.disks) > 0:
            if disk.rad > self.disks[-1].rad:
                print('큰 원반을 작은 원반 위로 옮길 수 없습니다.')
                return
        self.disks.append(disk) # 원반 리스트의 마지막에 추가
    
    def disk_out(self):
        if len(self.disks) == 0:
            print('원반이 없습니다.')
            return  
        return self.disks.pop()    # 원반 리스트의 마지막에서 삭제하고 반환
    
    def __str__(self):
        return self.name

def hanoi(diskNum, name1, name2, name3):
    source = Column(name1)
    middle = Column(name3)
    destination = Column(name2)
    for i in range(1, diskNum + 1):
        source.disk_in(Disk(i))

# 예시 
hanoi(3, 'A', 'C', 'B')

# A번 기둥의 1번 원반을 B번 기둥에 옮긴다.
# A번 기둥의 2번 원반을 B번 기둥에 옮긴다.
# B번 기둥의 1번 원반을 B번 기둥에 옮긴다.
# A번 기둥의 3번 원반을 C번 기둥에 옮긴다.
# B번 기둥의 1번 원반을 B번 기둥에 옮긴다.
# B번 기둥의 2번 원반을 C번 기둥에 옮긴다.
# B번 기둥의 1번 원반을 C번 기둥에 옮긴다.
