from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('job/', include('jobs.urls')),
    path('', include('jwt_auth.urls')),
]
