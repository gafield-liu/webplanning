from django.apps import AppConfig

# 注册类，网站运行的时候不会运行到apps.py文件
class BookConfig(AppConfig):
    name = 'book'
    verbose_name = '图书管理'
