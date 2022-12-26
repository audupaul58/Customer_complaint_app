from django.urls import path
from .views import LoginUser, LogOutUser, Register



urlpatterns =[
    path('', LoginUser.as_view(), name='login'),
    path('logout', LogOutUser.as_view(), name='logout'),
    path('register', Register.as_view(), name='register'),
]