from django.db import models
from luffyapi.utils.models import BaseModel


# Create your models here.
class Banner(BaseModel):
    name = models.CharField(max_length=32, verbose_name='图片名字')
    img = models.ImageField(upload_to='banner', verbose_name='轮播图',
                            help_text='图片尺寸3840*800', null=True)
    link = models.CharField(max_length=32, verbose_name='跳转连接')
    info = models.TextField()

    def __str__(self):
        return self.name
