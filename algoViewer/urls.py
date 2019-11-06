from django.urls import path
from algoViewer.views import HomeView

urlpatterns = [
    path('', HomeView.as_view()),
]
