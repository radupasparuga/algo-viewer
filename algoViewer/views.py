from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = "home.html"

class SortView(TemplateView):
	template_name = "sort.html"