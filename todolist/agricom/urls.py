from django.urls import path
from .views import AllNumbers, DeleteNumber, AddNumber, UpdateNumber, Search_Page


urlpatterns = [
    path('', AllNumbers.as_view(), name='agricom'),
    path('addnum/', AddNumber.as_view(), name='add-agricom'),
    path('search/', Search_Page.as_view(), name='search_agr'),
    path('update/<int:pk>/', UpdateNumber.as_view(), name='update-agricom'),
    path('delete/<int:pk>/', DeleteNumber.as_view(), name='delete-agricom'),
]