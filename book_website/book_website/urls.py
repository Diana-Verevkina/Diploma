from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]
