from django.db import models

# Create your models here.
from django.db import models
from captcha.fields import CaptchaField

class User(models.Model):
    username = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=20)
    captcha = CaptchaField() # 验证码字段，使用 django-simple-captcha 提供的 CaptchaField
    def __str__(self):
        return self.username