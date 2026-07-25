from django.urls import path
from . import views
from .api_views import PredictionListAPI

urlpatterns = [
    path("", views.home, name="home"),
    path("history/", views.history, name="history"),
    path(
        "api/predictions/",
        PredictionListAPI.as_view(),
        name="api_predictions"
    ),
]