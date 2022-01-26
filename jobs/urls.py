from django.urls import path
from .views import (
JobDetailView,
JobListView,
ApplicationListView,
ApplicationDetailView,
)

urlpatterns = [
    path('', JobListView.as_view()),
    path('<int:pk>/', JobDetailView.as_view()),
    path('<int:pk>/applications/', ApplicationListView.as_view()),
    path('<int:job_pk>/applications/<int:pk>/', ApplicationDetailView.as_view())
]
