from django.urls import path
from .views import HomeView, DetailView

app_name = "redisapp"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('detail/<int:id>', DetailView.as_view(), name="detail")
]