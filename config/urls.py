from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Администрирование VseLagerya"
admin.site.index_title = "Панель управления"
admin.site.site_title = "Админка VseLagerya"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/users/', include('users.urls')),
    path('api/camps/', include('camps.urls')),
    path('api/discounts/', include('discounts.urls')),
    path('api/orders/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
