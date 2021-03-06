"""ajaxproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from demoapp import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),  # rest framework urls.py file include
    path('admin/', admin.site.urls),
    path('', views.StudentView, name=''),
    path('stud-api', views.StudView.as_view(), name='stud-api'),
    path('stud-api<int:pk>', views.StudViewCrud.as_view(), name='stud-api'),
   
]
