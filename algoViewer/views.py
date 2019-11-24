from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = "home.html"

class SortView(TemplateView):
	template_name = "sort.html"

class PathfindingView(TemplateView):
	template_name= "pathfinding.html"

class SearchView(TemplateView):
	template_name= "search.html"
