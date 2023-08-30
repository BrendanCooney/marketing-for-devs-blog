from . import views
from django.urls import path
from about.views import welcome

urlpatterns = [
    path('', views.about_me, name='about'),
    path('welcome/', views.welcome, name ='welcome')
]