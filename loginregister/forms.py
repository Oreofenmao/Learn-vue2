from django import forms
from .models import User
from captcha.fields import  CaptchaField
#在ModelForm中，Meta类用于指定该表单与数据库模型之间的关系
class UserForm(forms.ModelForm):
    captcha = CaptchaField() #添加验证码字段
    class Meta:
        model = User
        #model = User：指定该表单关联的模型是 User
        fields = ['username','password','captcha']
        #fields=[] 定义哪些字段将出现在表单中