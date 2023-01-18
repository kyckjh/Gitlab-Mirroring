cnt = 0
password = 'qwerty123456'
while(cnt<3):
    password_input = input('비밀번호를 입력하세요 : ')
    if password_input == password:
        print('로그인 되었습니다.')
        break
    else:
        print('비밀번호가 틀렸습니다.')
        cnt += 1
if cnt == 3:
    print('3번 이상 비밀번호 입력에 실패하셨습니다.')