from django.urls import path
from .views import AllNumbers, DeleteNumber, AddNumber, UpdateNumber, Search_Page


urlpatterns = [
    path('', AllNumbers.as_view(), name='polcom'),
    path('addnum/', AddNumber.as_view(), name='add-polcom'),
    path('search/', Search_Page.as_view(), name='search_pol'),
    path('update/<int:pk>/', UpdateNumber.as_view(), name='update-polcom'),
    path('delete/<int:pk>/', DeleteNumber.as_view(), name='delete-polcom'),
]