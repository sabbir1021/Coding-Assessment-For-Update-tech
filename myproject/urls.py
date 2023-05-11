from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


# swagger Schema
schema_view = get_schema_view(
    openapi.Info(
        title="Update tech Test",
        default_version="1.0.1",
        description="Api description",
        contact=openapi.Contact(email="sabbirdev45@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('sales/', include('sales.urls', namespace='sales')),

    path('__debug__/', include('debug_toolbar.urls')),
    # swagger URL
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]
