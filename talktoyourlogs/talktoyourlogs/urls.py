"""
URL configuration for talktoyourlogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", upload),
    path("upload", upload),
    path("demo", demo),
    path("prompt", chat),
    path("history", get_history),
    path("category/<str:category>", category),
    path("get_categories", get_categories),
    path("suggest_similar", suggest_similar),

    path("internal", internal_endpoint),
    path("check", check_for_result),


]
