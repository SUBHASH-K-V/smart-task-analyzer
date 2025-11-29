"""
URL configuration for backend project.

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

from pathlib import Path

from django.contrib import admin  # type: ignore[import]
from django.http import FileResponse, Http404  # type: ignore[import]
from django.urls import include, path  # type: ignore[import]


BASE_DIR = Path(__file__).resolve().parent.parent


def frontend_index(request):
    """Serve the main frontend page from the frontend folder."""
    index_path = BASE_DIR / "frontend" / "index.html"
    if not index_path.exists():
        raise Http404("Frontend index.html not found")
    return FileResponse(open(index_path, "rb"))


def frontend_styles(request):
    """Serve the frontend CSS file."""
    css_path = BASE_DIR / "frontend" / "styles.css"
    if not css_path.exists():
        raise Http404("styles.css not found")
    return FileResponse(open(css_path, "rb"))


def frontend_script(request):
    """Serve the frontend JS file."""
    js_path = BASE_DIR / "frontend" / "script.js"
    if not js_path.exists():
        raise Http404("script.js not found")
    return FileResponse(open(js_path, "rb"))


urlpatterns = [
    # Frontend UI at root (no CORS issues – same origin as the API)
    path("", frontend_index, name="home"),
    path("styles.css", frontend_styles, name="frontend-styles"),
    path("script.js", frontend_script, name="frontend-script"),
    # Admin and API
    path("admin/", admin.site.urls),
    path("api/tasks/", include("tasks.urls")),
]
