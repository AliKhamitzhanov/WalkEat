from django.urls import path
from .views import FitListView, FitDetailView


urlpatterns = [
    path("fit/", FitListView.as_view()),
    path("fit/<int:pk>/", FitDetailView.as_view())
]

