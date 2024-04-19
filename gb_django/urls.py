from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_lesson1.urls')),
    path('lesson2/', include('app_lesson2.urls')),  
]  

