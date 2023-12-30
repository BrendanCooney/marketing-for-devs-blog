from . import views
from django.urls import path

urlpatterns = [
    path('tools/', views.ToolsList.as_view(), name='tools'),
] 