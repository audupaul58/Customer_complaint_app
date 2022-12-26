from django.urls import path
from .views import HomePage, AdminView, TaskListView, TaskCreateView, UpdateTask, DeleteTask, Search_Page


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('list/', TaskListView.as_view(), name='tasklist'),
    path('search/', Search_Page.as_view(), name='search'),
    path('admins/', AdminView.as_view(), name='admins'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateTask.as_view(), name='update_task'),
    path('delete/<int:pk>/', DeleteTask.as_view(), name='delete_task'),
    
]