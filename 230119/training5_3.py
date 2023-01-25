# 입력 예시
s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'

# 출력 예시
# 'I never dreamed about success, i worked for it.'
s = s[3:-3] # 특수문자 제거
s = "'" + s.lower().capitalize() + "'" # 소문자로 바꾸고 양쪽에 ' 추가
print(s)