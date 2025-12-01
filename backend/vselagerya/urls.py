from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# DRF router
from rest_framework import routers

# import routers from apps (we will create these)
from users.api import UserViewSet
from camps.api import CampViewSet, ShiftViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'camps', CampViewSet, basename='camp')
router.register(r'shifts', ShiftViewSet, basename='shift')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # optional: auth browsable API
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
