from . import views
from django.urls import path

urlpatterns = [
    path('tools/', views.ToolsList.as_view(), name='tools'),
    path('<slug:slug>/', views.tools_detail, name='tools_detail'),
] 