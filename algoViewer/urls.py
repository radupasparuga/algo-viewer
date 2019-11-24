from django.urls import path
from algoViewer.views import HomeView
from algoViewer.views import SortView
from algoViewer.views import PathfindingView
from algoViewer.views import SearchView

urlpatterns = [
    path('', HomeView.as_view()),
    path('sort', SortView.as_view()),
    path('pathfinding', PathfindingView.as_view()),
    path('search', SearchView.as_view()),
]
