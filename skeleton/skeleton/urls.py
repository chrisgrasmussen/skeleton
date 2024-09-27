"""
URL configuration for skeleton project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include, re_path
from start import views
from start.views import MyTokenObtainPairView
from rest_framework.urlpatterns import format_suffix_patterns
from complete import views as complete_views


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/start/', views.start_list),
    path('api/start/<int:pk>/', views.start_detail),
    
    path('api/start/<int:pks>/complete/', complete_views.complete_list),
    path('api/start/<int:pks>/complete/<int:pkc>/', complete_views.complete_detail),
    path('api/complete/<int:pk>', complete_views.complete_detail),
    
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)