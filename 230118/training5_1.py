import random

def making_card_list() -> list:
	card_list = []

	for shape in ["spade", "heart", "diamond", "clover"]:

		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

			card_list.append((shape, number))

	return card_list

trump_card_list = making_card_list()

# 카드를 tuple로 받아서 tuple1이 더 크면 True return
def compare_card(tuple1, tuple2):
    if tuple1[1] == tuple2[1]:
        return compare_shape(tuple1[0], tuple2[0])
    else:
        return compare_number(tuple1[1], tuple2[1])

# number1이 number2보다 크면 True return
def compare_number(number1, number2):
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    return numbers.index(number1) > numbers.index(number2)

# shape1이 shape2보다 크면 True return
def compare_shape(shape1, shape2):
    shapes = ["clover", "heart", "diamond", "spade"]
    return shapes.index(shape1) > shapes.index(shape2)

# 카드 섞기
def shuffle(card_list):
    for i in range(len(card_list)-1):
        rand_index = random.randrange(i+1, len(card_list))
        card_list[i], card_list[rand_index] = card_list[rand_index], card_list[i]

score1 = 0
score2 = 0

while(score1 < 6 and score2 < 6):   # 두 플레이어 중 한 명의 점수가 6이 되면 종료
    shuffle(trump_card_list)
    # 카드 한 장씩 뽑고 리스트에서 제거
    player1 = trump_card_list[0]    
    del trump_card_list[0]
    player2 = trump_card_list[0]
    del trump_card_list[0]
    
    result = compare_card(player1, player2)     # player1이 이기면 result = True
    print(f'{player1} {player2} player{1 if result else 2} win!')
    score1 += result        # result = True이면 + 1, False이면 + 0
    score2 += not result
    
print(f'{score1}:{score2} Finally player{1 if score1 > score2 else 2} win')