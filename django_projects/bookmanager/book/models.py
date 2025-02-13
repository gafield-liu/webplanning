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
    name = models.CharField(max_length=20, verbose_name="书籍名称")  # verbose 表示别名，显示在admin后台
    pub_date = models.DateField(verbose_name="发布日期", null=True)  # null=True字段允许为空
    readcount = models.IntegerField(verbose_name="阅读量", default=0)
    commentcount = models.IntegerField(default=0, verbose_name="评论量")

    # 逻辑删除（假删除，数据库中存在）
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")
    # 物理删除（真实删除）

    def __str__(self):
        return self.name

    # 内部类:admin 后台取中文名，or 给表重命名
    class Meta:
        verbose_name = "书籍管理"
        # admin 中删除s后缀
        verbose_name_plural = verbose_name
        # 给表重命名 app-name_model-name book_bookinfo
        db_table = 'bookinfo'




#  人物表 和 书籍 多对一 的关系
class PeopleInfo(models.Model):

    # 性别，枚举类型
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female'),
    )
    name = models.CharField(max_length=10, verbose_name="人物名称")
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name="性别")
    description = models.TextField(max_length=200, null=True, verbose_name="描述信息")

    # 声明外键,约束作用,随主键删除而删除，如果是PROTECT，不允许删除
    # 外键查询速度过慢，大型项目中不建议使用
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name="书籍")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "人物信息"
        # admin 中删除s后缀
        verbose_name_plural = verbose_name
        db_table = "peopleinfo"




