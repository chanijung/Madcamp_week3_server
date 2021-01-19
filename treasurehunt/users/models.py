from django.db import models
from django.contrib.auth.models import AbstractUser
# from django..models import ListCharField

class User(AbstractUser):
    """ Custom User Model"""
    uid = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    LOGIN_FACEBOOK = "FaceBook"
    LOGIN_CHOICES = ((LOGIN_FACEBOOK, "FaceBook"), )
    login_method = models.CharField(choices=LOGIN_CHOICES,max_length=20,default=LOGIN_FACEBOOK)
    nickname = models.CharField(max_length=15, blank=True, null=True)
    token = models.CharField(max_length=255, default='unknown token')
    score = models.IntegerField(default=0)
    close_treasure = models.IntegerField(blank=True, null=True)

    def serialize_custom(self):
        data = {
            "nickname" : self.nickname,
            "score" : self.score,
        }
        return data