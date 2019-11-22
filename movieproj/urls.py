
from django.contrib import admin
from django.urls import path,include
# from rest_framework.schemas import get_schema_view
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view=get_swagger_view(title="Movie Operation API")

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include('rest_framework.urls')),
    url('v1/',include('movieap.urls')),
    url('apidoc/',schema_view)
]
