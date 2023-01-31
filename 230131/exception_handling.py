# 예외를 처리하는 방법
# 1. 예외 상황을 만들지 않기
# if, for while 등 조건문이 들어가는 구문을 통해서 예외 상황 방지

# 2. 예외가 발생하면 무슨 일을 해야 할 지 알려주기
# try - except( - finally) 구문
try:
    # 실행할 문장
    pass
except 예외종류:
    #예외 발생 시 실행할 문장
    pass