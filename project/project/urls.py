from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('class_based_views_app/', include('class_based_views_app.urls')),
]
