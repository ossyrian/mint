"""
URL configuration for mint project.
"""

from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


def home(request):
    """Home page with game database focus."""
    return render(request, "home.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    # Versioned API URLs
    path("api/<str:version>/", include("api.urls")),
    # Versioned OpenAPI schema
    path(
        "api/<str:version>/schema/",
        SpectacularAPIView.as_view(),
        name="schema-versioned",
    ),
    path(
        "api/<str:version>/docs/",
        SpectacularSwaggerView.as_view(url_name="schema-versioned"),
        name="swagger-ui-versioned",
    ),
    # Domain Apps
    path("", home, name="home"),
    path("db/", include("minty_db.urls")),
    path("mogul/", include("minty_mogul.urls")),
    path("guilds/", include("minty_hq.urls")),
]
