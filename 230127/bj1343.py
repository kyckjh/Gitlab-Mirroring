input_str = input()
board = list(map(str, input_str.split('.')))
board2 = list(map(str, input_str.split('X')))
while '' in board:
    board.remove('')
while '' in board2:
    board2.remove('')
result_list = []
bool_result = True
if len(board) == 0:
    print(board2[0])
    bool_result = False
else:
    for sep in board:
        if sep.find('X') != -1:
            result = ''
            length = len(sep)
            div_4 = length // 4
            mod_4 = length % 4
            result += 'AAAA' * div_4
            if mod_4 == 2:
                result += 'BB'
            elif mod_4 != 0:
                bool_result = False
                print(-1)
                break
            result_list.append(result)

if bool_result:
    if input_str[0] == 'X':
        while True:        
            if len(board2) == 0:
                try:
                    print(result_list.pop(0)) 
                    break  
                except:
                    break  
            print(result_list.pop(0), board2.pop(0), sep='', end='')
    else:
        while True:
            if len(result_list) == 0:     
                try:
                    print(board2.pop(0))  
                    break     
                except:
                    break
            print(board2.pop(0), result_list.pop(0), sep='', end='')
        