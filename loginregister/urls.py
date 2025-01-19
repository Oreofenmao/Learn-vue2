from django.urls import path
from . import views
from captcha.views import captcha_image
urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    path('captcha/', captcha_image  , name='captcha'),
]