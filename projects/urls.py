
from django.urls import path
from .views import (
    hello, 
    projects, 
    project
)


urlpatterns = [
    path('', hello),
    path('projects/', projects),
    path('projects/<int:pk>', project),
]
