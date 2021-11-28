from rest_framework import serializers
from . import models
class BannerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = ['name','img','link']