
from django.urls import path
from book.views import index, index_html
# 子路由
urlpatterns = [
    path('home/', index),
    path('index_html/', index_html),

]