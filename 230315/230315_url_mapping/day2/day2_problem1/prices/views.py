from django.shortcuts import render

# Create your views here.
def price(request, thing, cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    context = {
        'thing':thing,
        'cnt':cnt,
        'price':-1,
    }
    if thing in product_price:
        context['price'] = product_price[thing]*cnt
    return render(request, 'price.html', context)