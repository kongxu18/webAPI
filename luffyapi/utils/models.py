from django.db import models


# 一些基本字段抽出来
class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True
                                       , verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True
                                       , verbose_name='更新时间')
    is_delete = models.BooleanField(default=False,
                                    verbose_name='是否删除')
    is_show = models.BooleanField(default=True,
                                  verbose_name='是否展示')
    display_order = models.IntegerField()

    class Meta:
        # 不加入数据库
        abstract = True
