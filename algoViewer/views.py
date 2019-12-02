from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from .handlers import sort_file_handler
from .forms import SortForm

def sort_file(request):
	if request.method == 'POST':
		form = SortForm(request.POST, request.FILES)
		if form.is_valid():
			sort_file_handler(form.cleaned_data)
			response = HttpResponse()
			response['Content-Disposition'] = 'attachment; filename="output.txt"'
			return response
		else:
			print("data not valid")
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
