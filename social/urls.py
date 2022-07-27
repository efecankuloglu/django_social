from django.urls import path

from .views import MainPageView, profile_view

app_name = "social"

urlpatterns = [
    path("", MainPageView.as_view(), name="main-page"),
    path("<slug:slug>/", profile_view, name="profile")
]
