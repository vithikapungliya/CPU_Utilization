from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.urls import include, re_path
# from django.conf.urls import url
from django.conf import settings
urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('', include('chat.urls')),
    re_path('', include('chat.urls'))
]
