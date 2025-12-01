from django.urls import path
from .views import CampListView, CampDetailView, CampProgramsView

urlpatterns = [
    path("", CampListView.as_view(), name="camp_list"),
    path("<int:pk>/", CampDetailView.as_view(), name="camp_detail"),
    path("<int:camp_id>/programs/", CampProgramsView.as_view(), name="camp_programs"),
]
