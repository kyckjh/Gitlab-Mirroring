from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, 'articles/throw.html')

def catch(request): # 인자로 받는 request 객체가 요청 정보 포함
    # 클라이언트로부터 요청파라미터에 담겨져서 전달된 데이터는
    # request 정보에 포함되어 있음
    message = request.POST.get('message')
    context = {
        'message' : message
    }
    return render(request, 'articles/catch.html')