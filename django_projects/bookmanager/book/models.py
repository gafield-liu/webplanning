from django.db import models

# Create your models here.

"""
1. 创建模型类，继承 models.Model 
2. 系统会自动帮助我们创建主键
3. 字段
    表中的字段名 需要有类型
    models.字段类型（CharField）

mysql: 
    varchar: strr
    varchar(M):代表当前字段数据的长度

id: django orm 自动创建主键
"""


# Create your views here.
class BookInfo(models.Model):
    # 创建字段
    name = models.CharField(max_length=10, verbose_name="书籍名称")

    # 内置函数方法
    # 用在admin后台管理系统中的，显示出name字段（比如显示西游记）
    def __str__(self):
        return self.name

    # 内部类:修改当前模型的
    class Meta:
        verbose_name = "书籍管理"
        # admin 中删除s后缀
        verbose_name_plural = verbose_name



#  人物表 和 书籍 多对一 的关系
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10, verbose_name="人物名称")
    gender = models.BooleanField(verbose_name="性别")

    # 外键 随着 xx 删除而删除
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name="所属类别")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "人物管理"
        # admin 中删除s后缀
        verbose_name_plural = verbose_name


