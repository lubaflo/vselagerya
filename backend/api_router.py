# backend/api_router.py

from rest_framework import routers
from camps.views import CampViewSet, ProgramViewSet, DocumentViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()

# ---- CAMPS ----
router.register(r'camps', CampViewSet, basename='camps')
router.register(r'programs', ProgramViewSet, basename='programs')
router.register(r'documents', DocumentViewSet, basename='documents')

# ---- USERS ----
router.register(r'users', UserViewSet, basename='users')

urlpatterns = router.urls
