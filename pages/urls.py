from django.urls import path
from .views import HomePageView, aboutPageView


urlpatterns = [
    path("", HomePageView.as_view(),name="home" ),
    path("about/", aboutPageView.as_view(),name="about" ),
]