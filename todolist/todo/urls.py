from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('categories', views.cats, name='cats'),
    path('addTask', views.create, name='addTask'),
    path('task/<int:taskid>/', views.task, name='task'),
    path('cat/<int:catid>/', views.category, name='category'),

]
