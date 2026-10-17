"""
URL configuration for stu_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
#
from controller import PageController as pc
from controller import SystemController as sc
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #
    #
    path("goA/",pc.go_a),
    path("",pc.go_login),
    path("goSystem/",pc.go_system),
    path("goImgDetect/",pc.go_imDetect),
    path("goDetectImg/",pc.go_imDetect),
    #
    path("login/",sc.login),
    path("imgDetect/",sc.img_detect),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
