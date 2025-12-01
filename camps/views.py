from rest_framework import generics, permissions
from .models import Camp, Program
from .serializers import CampSerializer, ProgramSerializer


class CampListView(generics.ListAPIView):
    queryset = Camp.objects.filter(is_verified=True)
    serializer_class = CampSerializer


class CampDetailView(generics.RetrieveAPIView):
    queryset = Camp.objects.filter(is_verified=True)
    serializer_class = CampSerializer


class CampProgramsView(generics.ListAPIView):
    serializer_class = ProgramSerializer

    def get_queryset(self):
        camp_id = self.kwargs["camp_id"]
        return Program.objects.filter(camp_id=camp_id)
