from django.urls import path
from algoViewer.views import HomeView
from algoViewer.views import SortView

urlpatterns = [
    path('', HomeView.as_view()),
    path('sort', SortView.as_view()),
]
