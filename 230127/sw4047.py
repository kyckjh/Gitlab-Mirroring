# import copy
T = int(input())
for test_case in range(1, T + 1):
    S = input()
    # shapes = ['S', 'D', 'H', 'C']
    card_dict = {}
    # for shape in shapes:
    #     card_dict[shape] = copy.deepcopy(list(range(1,14)))
    card_dict['S'] = list(range(1,14))
    card_dict['D'] = list(range(1,14))
    card_dict['H'] = list(range(1,14))
    card_dict['C'] = list(range(1,14))
    for i in range(0, len(S), 3):
        try:
            card_dict[S[i]].remove(int(S[i+1]+S[i+2]))
        except:            
            print(f'#{test_case}', 'ERROR')
            break
    else:
        print(f'#{test_case}', end=' ')
        for cards in card_dict.values():
            print(len(cards), end=' ')
        print()
# 3
# S01D02H03H04
# H02H10S11H02
# S10D10H10C01