from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SortForm

def sort_file(request):
	if request.method == 'POST':
		form = SortForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/')
	else:
		form = SortForm()
	return render(request, 'sort.html', {'form': form})

class HomeView(TemplateView):
	template_name = "home.html"

class SortView(TemplateView):
	template_name = "sort.html"

class PathfindingView(TemplateView):
	template_name= "pathfinding.html"

class SearchView(TemplateView):
	template_name= "search.html"
