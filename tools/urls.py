from . import views
from django.urls import path

urlpatterns = [
    path('tools/', views.about_me, name='tools'),
] 