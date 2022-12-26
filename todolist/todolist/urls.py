
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('access.urls')),
    path('todo/', include('todos.urls')),
    path('polcom/', include('polcom.urls')),
    path('agricom/', include('agricom.urls')),
]
