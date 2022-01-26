from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from.permissions import isOwnerOrReadyOnly

from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer

class JobListView(ListCreateAPIView):
    ''' View for /job endpoint GET/POST '''

    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class JobDetailView(RetrieveUpdateDestroyAPIView):
    ''' View for /job/id endpoint GET/PUT/PATCH/DELETE'''

    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class ApplicationListView(CreateAPIView):
    ''' View for /job/id/application POST'''

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
class ApplicationDetailView(DestroyAPIView):
    ''' View for /job/id/application/applicationId DELETE'''

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (isOwnerOrReadyOnly, )
    