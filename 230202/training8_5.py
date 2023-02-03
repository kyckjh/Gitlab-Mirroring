class Disk: # 원반
    def __init__(self, rad:int): # rad : 크기
        self.rad = rad
    
    def __str__(self):
        return f'{self.rad}번 원반'
        
class Column:   # 기둥
    def __init__(self, name):
        self.name = name    # Column 인스턴스 이름
        self.disks = []     # Column 에 들어있는 원반 리스트
    
    # Column 인스턴스의 디스크 목록(self.disks)에 원소(Disk 인스턴스)를 추가하는 함수
    def disk_in(self, disk:Disk):
        if len(self.disks) > 0:
            if disk.rad > self.disks[-1].rad:
                print('큰 원반을 작은 원반 위로 옮길 수 없습니다.')
                print(f'옮기려는 원반 : {disk} 맨 위 원반 :  {self}의 {self.disks[-1]}')
                return               
        self.disks.append(disk) # 원반 리스트의 마지막에 추가
    
    # Column 인스턴스가 가진 디스크 목록을 보여주는 함수
    def get_disks_list(self):
        if len(self.disks) > 0:
            print(f'{self}의 디스크 목록 : ', end='')
            for dd in self.disks:
                print(dd.rad, end=' ')
            print()
        else:
            print(f'{self}에 원반이 없습니다.')

    # Column 인스턴스의 디스크 목록(self.disks)에서 맨 뒤 원소를 제거하는 함수
    def disk_out(self):
        if len(self.disks) == 0:
            print('원반이 없습니다.')
            return  
        return self.disks.pop()    # 원반 리스트의 마지막에서 삭제하고 반환
    
    def __str__(self):
        return f'{self.name}번 기둥'

# column_from의 맨 위 원반을 column_to로 옮기는 함수
def move_disk(column_from:Column, column_to:Column):
    tempDisk = column_from.disk_out()
    column_to.disk_in(tempDisk)
    print(f'{column_from}의 {tempDisk}을 {column_to}에 옮긴다')

# 하노이 퍼즐 풀이 함수
def hanoi_al(n, c_from, c_to, c_mid):
    if n == 1:  # 위에 원반이 없으면 원반을 바로 목적지로 옮기기
        move_disk(c_from, c_to)
        return 
    
    # 위의 원반을 모두 중간지점으로 옮기기
    hanoi_al(n - 1, c_from, c_mid, c_to)    
    # 원반을 목적지로 옮기기
    move_disk(c_from, c_to)    
    # 중간지점의 원반을 목적지로 다시 모두 옮기기
    hanoi_al(n - 1, c_mid, c_to, c_from)

    
def hanoi(diskNum, name1, name2, name3):
    # 기둥 3개 생성
    source = Column(name1)
    middle = Column(name3)
    destination = Column(name2)
    # 출발점 기둥에 원반 diskNum 개수만큼 큰 순서대로 추가
    for i in range(diskNum, 0, -1):
        source.disk_in(Disk(i))
    hanoi_al(diskNum, source, destination, middle)
    
    print()
    source.get_disks_list()
    middle.get_disks_list()
    destination.get_disks_list()

# 예시 
hanoi(6, 'A', 'C', 'B')

# A번 기둥의 1번 원반을 B번 기둥에 옮긴다.
# A번 기둥의 2번 원반을 B번 기둥에 옮긴다.
# B번 기둥의 1번 원반을 B번 기둥에 옮긴다.
# A번 기둥의 3번 원반을 C번 기둥에 옮긴다.
# B번 기둥의 1번 원반을 B번 기둥에 옮긴다.
# B번 기둥의 2번 원반을 C번 기둥에 옮긴다.
# B번 기둥의 1번 원반을 C번 기둥에 옮긴다.
