from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("health/", views.health_check, name="health"),
    path("analyze/", views.analyze_tasks, name="analyze"),
    path("suggest/", views.suggest_tasks, name="suggest"),
]



