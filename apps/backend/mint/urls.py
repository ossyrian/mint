"""
URL configuration for mint project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    # Versioned API URLs
    path("api/<str:version>/", include("api.urls")),
    # Versioned OpenAPI schema
    path("api/<str:version>/schema/", SpectacularAPIView.as_view(), name="schema-versioned"),
    path(
        "api/<str:version>/docs/",
        SpectacularSwaggerView.as_view(url_name="schema-versioned"),
        name="swagger-ui-versioned",
    ),
    # Frontend URLs
    path("", include("frontend.urls")),
]
