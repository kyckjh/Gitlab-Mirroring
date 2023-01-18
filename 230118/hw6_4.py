# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

input_list = ['eat','tea','tan','ate','nat','bat']

def group_anagrams(input_list):
    set_dict = {}   # input_list 의 index를 key로, 원소를 set으로 바꾼 dict
    for idx, word in enumerate(input_list):
        word_set = set()            # 단어의 각 글자 하나씩 원소로 가지는 set
        for char in word:
            word_set.add(char)
        set_dict[idx] = word_set

    result = [] # 결과를 넣을 list

    while(len(set_dict) > 0):
        tempList = []   # result 한 칸에 들어갈 단어들을 넣을 list
        poplist = []    # tempList에 추가한 인덱스들을 빼주기 위한 index를 모은 list
        first_idx = list(set_dict.keys())[0]    # set_dict의 키 중 하나를 가져옴   
        for idx in set_dict:
            if set_dict[first_idx] == set_dict[idx]:
                tempList.append(input_list[idx])
                poplist.append(idx)
        for i in poplist:
            set_dict.pop(i)
        result.append(tempList)   
        
    return result

print(group_anagrams(input_list))