"""core URL Configuration

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

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views import debug
from django.views.generic import TemplateView

from .api_v1 import api

handler400 = TemplateView.as_view(template_name="errors/400.html")
handler403 = TemplateView.as_view(template_name="errors/403.html")
handler404 = TemplateView.as_view(template_name="errors/404.html")
handler500 = TemplateView.as_view(template_name="errors/500.html")

urlpatterns = [
    path("", debug.default_urlconf),
    #   Admin Site
    # ================
    path("admin/", admin.site.urls),
    #   Errors
    # ===========
    path("400/", handler400),
    path("403/", handler403),
    path("404/", handler404),
    path("500/", handler500),
    #   HTTP
    # =========
    path("user/", include("apps.user.urls")),
    #   Api
    # ========
    path("api/v1/", api.urls),
]
if settings.DEBUG:
    urlpatterns += (path("__debug__/", include("debug_toolbar.urls")),)