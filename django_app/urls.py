"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_app import settings
from django.conf.urls.static import static
#from app_name.views import {all the views}
#from app_name.models import {all the models}
#from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#The routers registered and listed here will provide the routes to each viewset
'''
router = routers.DefaultRouter()
router.register(r'route_name', route_Model_NameViewSet)
---repeat for each needed--- then uncomment
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include(router.urls)),
    #path('app_name/' include('app_name.urls')),
    #path('api-auth/' include('rest_framework.urls', name='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
