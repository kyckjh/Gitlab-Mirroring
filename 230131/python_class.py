def emoji_decorator(func):
    def wrapper(name):
        func(name)
        print('^~^//')
    
    return wrapper

@emoji_decorator
def ko_hello(name):
    print(f'안녕하세요, {name}님!')

@emoji_decorator
def en_hello(name):
    print(f'Hello, {name}!')
   
ko_hello('aiden')   
# 안녕하세요, aiden님!
# ^~^//
en_hello('aiden')   
# Hello, aiden!
# ^~^//