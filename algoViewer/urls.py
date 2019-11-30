from django.urls import path
from algoViewer.views import HomeView
from algoViewer.views import SortView
from algoViewer.views import PathfindingView
from algoViewer.views import SearchView
from algoViewer.views import sort_file

urlpatterns = [
    path('', HomeView.as_view()),
    path('sort', sort_file,),
    path('pathfinding', PathfindingView.as_view()),
    path('search', SearchView.as_view()),
]
