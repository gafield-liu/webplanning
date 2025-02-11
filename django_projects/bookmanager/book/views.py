import http
from django.shortcuts import render
from django.http import HttpResponse
# from django.http import HttpRequest
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index_html(request):
    user_info = {
        'username': 'gafield'
    }
    return render(request, 'book/index.html', context=user_info)  #通过 context 将数据库中的数据渲染到html
