from django.urls import path
# from django.contrib.auth.views import LoginView
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.home_page, name="home"),
    path('register/', views.register, name='register')
    #TODO: login without register url
]
