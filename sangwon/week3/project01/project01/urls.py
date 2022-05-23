"""project01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from namecard import views as nmViews
from assign1 import views as as1Views
from assign2 import views as as2Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('namecard/', nmViews.index, name="index"),
    path('assign1/', as1Views.index, name="assign"),
    path('assign1/good', as1Views.postgood, name="good"),
    path('assign2/', as2Views.index, name="main2"),
    path('assign2/good', as2Views.postgood, name="as2vgood")
]
